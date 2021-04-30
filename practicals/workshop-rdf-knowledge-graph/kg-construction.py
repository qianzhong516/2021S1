import os

os.system('python -m rdfizer -c ./config.ini')

import rdflib
g = rdflib.Graph()
res = g.parse("triples.nt", format="ntriples")
output = res.serialize(format='turtle').decode("utf-8")
print(output)

# What is the name of the personality that practises tennis?
# {"results": {"bindings": [{"who": {"type": "literal", "value": "Venus Williams"}}]}, "head": {"vars": ["who"]}}

res = g.query(
            """ PREFIX ns1: <http://xmlns.com/foaf/0.1/>
                PREFIX ns2: <http://example.com/ontology/>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT ?who
                WHERE { ?x ns1:name ?who .
                        ?x ns2:practises ?y .
                        ?y rdfs:label "Tennis" .
                      }
            """ )
print(res.serialize(format="json").decode("utf-8"))
