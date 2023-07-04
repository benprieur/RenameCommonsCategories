import pywikibot
from pywikibot import pagegenerators

site = pywikibot.Site(u'commons', u'commons')
site.login()

# move the current name to a new name
def move(title, newCategoryName, summary, noredirect=True):
    page = pywikibot.Category(site, title)
    try:
        page = pywikibot.site.APISite.movepage(
        site,
        page=page,
        newtitle=newCategoryName,
        summary=summary,
        noredirect=noredirect
    )
    except:
        print("bof man", newCategoryName)
        
    return page

# rename
def rename(cat):

    for subcat in cat.subcategories():
        
        # get title & text
        title = subcat.title()
        text = subcat.text
        newText = text.replace("Éxupéry", "Exupéry")

        # renaming subcat
        if subcat.text != newText:
            subcat.text = newText    
            subcat.save("Éxupéry", "Exupéry")
        
        titleTarget = title.replace("Éxupéry", "Exupéry")
        if titleTarget != title:

            # updating text of every page included in subcat
            subcatobj = pagegenerators.CategorizedPageGenerator(subcat)
            for page in subcatobj:
                print(page.title())
                text = page.text
                newText = text.replace("Éxupéry", "Exupéry")
                if page.text != newText:
                    page.text = newText    
                    page.save("Éxupéry > Exupéry: edit")

            # rename current subcat
            move(title, titleTarget, "Éxupéry > Exupéry: move")

        # recursive
        subcategory = pywikibot.Category(site, title)
        rename(subcategory)


category = pywikibot.Category(site, u'Lyon Saint-Exupéry Airport')
print(category)
rename(category)