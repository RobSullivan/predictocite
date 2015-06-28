

from ggplot import *
import pandas as pd

from predictocite.datasets.citation_groups import fetch_citations


articles = fetch_citations()

data = {'pmid':articles.pmid, 'citations':articles.citation_count}

citations = pd.DataFrame(data=data, columns=data.keys())

ggplot(citations, aes('pmids', 'citations')) +\
    geom_point(colour='steelblue')
