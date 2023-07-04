import pywikibot
from pywikibot import pagegenerators

site = pywikibot.Site(u'commons', u'commons')
site.login()

# move the current name to a new name - category
def moveCategory(title, newTitle, summary, noredirect=True):
    page = pywikibot.Category(site, title)
    try:
        page = pywikibot.site.APISite.movepage(
        site,
        page=page,
        newtitle=newTitle,
        summary=summary,
        noredirect=noredirect
    )
    except:
        print("bof man", newTitle)

    return page

# move the current name to a new name - file
def moveFile(title, newTitle, summary, noredirect=True):
    page = pywikibot.Page(site, title)
    try:
        page = pywikibot.site.APISite.movepage(
        site,
        page=page,
        newtitle=newTitle,
        summary=summary,
        noredirect=noredirect
    )
    except:
        print("bof man", newTitle)

    return page

# rename
def rename(cat):

    for subcat in cat.subcategories():
        
        # get title & text
        titleSource = subcat.title()
        text = subcat.text
        newText = text.replace("Éxupéry", "Exupéry")
        print(titleSource)

        # renaming subcat
        if subcat.text != newText:
            subcat.text = newText    
            subcat.save("Éxupéry > Exupéry: edit category")
        
        titleTarget = titleSource.replace("Éxupéry", "Exupéry")

        # updating text of every page included in subcat
        subcatobj = pagegenerators.CategorizedPageGenerator(subcat)
        for page in subcatobj:
            
            text = page.text
            newText = text.replace("Éxupéry", "Exupéry")
            newTitle = page.title().replace("Éxupéry", "Exupéry")

            if page.text != newText:
                page.text = newText    
                page.save("Éxupéry > Exupéry: edit file")

            if page.title() != newTitle:
                moveFile(page.title(), newTitle, "Éxupéry > Exupéry: move file", False)

        if titleTarget != titleSource:
            # rename current subcat
            moveCategory(titleSource, titleTarget, "Éxupéry > Exupéry: move category")

        # recursive
        subcategory = pywikibot.Category(site, titleSource)
        rename(subcategory)


category = pywikibot.Category(site, u'Lyon Saint-Exupéry Airport')
print(category)
rename(category)
