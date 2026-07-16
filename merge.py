import nbformat

nb1 = nbformat.read("notebook/01_sitemap.ipynb", as_version=4)
nb2 = nbformat.read("notebook/02_scraping_listing.ipynb", as_version=4)

nb1.cells.extend(nb2.cells)

nbformat.write(nb1, "notebook/scraping.ipynb")