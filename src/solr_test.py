import solr

s = solr.SolrConnection('http://localhost:8983/solr')

print s

s.add(id=12, title='Asf Test 2', author='Asf Test Author 1')
s.commit()

response = s.query('title:Asf author:Asf')
for hit in response.results:
    print hit['id'], hit['title']


print 'numFound:', response.numFound
print 'numFound (right way):', int(getattr(response, 'numFound', 0)) # Right way.
print 'start:', response.start


print response.results

    


#
## add a document to the index
#s.add(id=1, title='Lucene in Action', author=['Erik Hatcher', 'Otis Gospodnetic'])
#s.commit()
#
## do a search
#response = s.query('title:lucene')
#for hit in response.results:
#    print hit['title']