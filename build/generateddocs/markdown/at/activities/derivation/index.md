
# Derivation Activity (Schema)

`sop.at.activities.derivation` *v1.0*

A derivation activity takes a data set and derives a new data set from it. It must reference an Entity which defines the derivation function, allowing identification of the derivation process.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Derivation Activity 

This building block provides a JSON schema based on the PROV model for an activity derives new data using a function based on properties of that data. 






## Examples

### Derivation
Shows a derivation activity with a positive result.
#### json
```json
{
  "provType": [ "Activity", "Derivation" ],
  "id": "derivation_example",
  "endedAtTime": "2029-01-01T22:05:19+02:00",
  "wasAssociatedWith": "eg_agents:bc-3",
  "generated": { "id": "mydata:YearlySummary",
    "wasDerivedFrom" : "mydata:WeeklyRecords",
    "wasGeneratedBy" : "derivation_example"
  },
  "used": "mydata:WeeklyRecords"
}





```

#### jsonld
```jsonld
{
  "@context": [
    {
      "mydata": "http://example.com/datasets/"
    },
    "https://surroundaustralia.github.io/analytic-transparency/build/annotated/at/activities/derivation/context.jsonld"
  ],
  "provType": [
    "Activity",
    "Derivation"
  ],
  "id": "derivation_example",
  "endedAtTime": "2029-01-01T22:05:19+02:00",
  "wasAssociatedWith": "eg_agents:bc-3",
  "generated": {
    "id": "mydata:YearlySummary",
    "wasDerivedFrom": "mydata:WeeklyRecords",
    "wasGeneratedBy": "derivation_example"
  },
  "used": "mydata:WeeklyRecords"
}
```

#### ttl
```ttl
@prefix mydata: <http://example.com/datasets/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/activities/derivation_example> prov:endedAtTime "2029-01-01T22:05:19+02:00"^^xsd:dateTime ;
    prov:generated mydata:YearlySummary ;
    prov:used mydata:WeeklyRecords ;
    prov:wasAssociatedWith <http://example.com/activities/eg_agents:bc-3> .

mydata:YearlySummary prov:wasDerivedFrom mydata:WeeklyRecords ;
    prov:wasGeneratedBy <http://example.com/activities/derivation_example> .


```

## Schema

```yaml
description: Derivation activity
$defs:
  Derivation:
    allOf:
    - $ref: https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml#/$defs/Activity
    - properties:
        provType:
          type: array
          contains:
            type: string
            const: Derivation
      required:
      - provType
      - generated
      - used
anyOf:
- $ref: '#/$defs/Derivation'

```

Links to the schema:

* YAML version: [schema.yaml](https://surroundaustralia.github.io/analytic-transparency/build/annotated/at/activities/derivation/schema.json)
* JSON version: [schema.json](https://surroundaustralia.github.io/analytic-transparency/build/annotated/at/activities/derivation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "activityType": "@type",
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "wasAssociatedWith": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "agentType": "@type",
        "name": "rdfs:label",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedDelegation",
          "@type": "@id"
        },
        "provType": "@type"
      },
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "used": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "invalidated": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "generated": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:generated",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@context": {
            "featureType": "@type",
            "entityType": "@type",
            "has_provenance": {
              "@id": "dct:provenance",
              "@type": "@id"
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasDerivedFrom": {
              "@id": "prov:wasDerivedFrom",
              "@type": "@id"
            },
            "alternateOf": {
              "@id": "prov:alternateOf",
              "@type": "@id"
            },
            "hadPrimarySource": {
              "@id": "prov:hadPrimarySource",
              "@type": "@id"
            },
            "specializationOf": {
              "@id": "prov:specializationOf",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "links": {
              "@context": {
                "href": {
                  "@type": "@id",
                  "@id": "oa:hasTarget"
                },
                "rel": {
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  },
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id"
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              },
              "@id": "rdfs:seeAlso"
            },
            "qualifiedGeneration": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedGeneration",
              "@type": "@id"
            },
            "qualifiedInvalidation": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id"
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id"
            },
            "qualifiedAttribution": {
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAttribution",
              "@type": "@id"
            },
            "provType": "@type",
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          },
          "@id": "prov:entity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@context": {
            "featureType": "@type",
            "entityType": "@type",
            "has_provenance": {
              "@id": "dct:provenance",
              "@type": "@id"
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasDerivedFrom": {
              "@id": "prov:wasDerivedFrom",
              "@type": "@id"
            },
            "alternateOf": {
              "@id": "prov:alternateOf",
              "@type": "@id"
            },
            "hadPrimarySource": {
              "@id": "prov:hadPrimarySource",
              "@type": "@id"
            },
            "specializationOf": {
              "@id": "prov:specializationOf",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "links": {
              "@context": {
                "href": {
                  "@type": "@id",
                  "@id": "oa:hasTarget"
                },
                "rel": {
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  },
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id"
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              },
              "@id": "rdfs:seeAlso"
            },
            "qualifiedGeneration": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedGeneration",
              "@type": "@id"
            },
            "qualifiedInvalidation": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id"
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id"
            },
            "qualifiedAttribution": {
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAttribution",
              "@type": "@id"
            },
            "provType": "@type",
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          },
          "@id": "prov:entity",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@context": {
            "featureType": "@type",
            "entityType": "@type",
            "has_provenance": {
              "@id": "dct:provenance",
              "@type": "@id"
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasDerivedFrom": {
              "@id": "prov:wasDerivedFrom",
              "@type": "@id"
            },
            "alternateOf": {
              "@id": "prov:alternateOf",
              "@type": "@id"
            },
            "hadPrimarySource": {
              "@id": "prov:hadPrimarySource",
              "@type": "@id"
            },
            "specializationOf": {
              "@id": "prov:specializationOf",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "links": {
              "@context": {
                "href": {
                  "@type": "@id",
                  "@id": "oa:hasTarget"
                },
                "rel": {
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  },
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id"
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              },
              "@id": "rdfs:seeAlso"
            },
            "qualifiedGeneration": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedGeneration",
              "@type": "@id"
            },
            "qualifiedInvalidation": {
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id"
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id"
            },
            "qualifiedAttribution": {
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAttribution",
              "@type": "@id"
            },
            "provType": "@type",
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          },
          "@id": "prov:entity",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@context": {
        "agent": {
          "@context": {
            "agentType": "@type",
            "name": "rdfs:label",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@context": {
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedDelegation",
              "@type": "@id"
            },
            "provType": "@type"
          },
          "@id": "prov:agent",
          "@type": "@id"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "hadPlan": {
          "@id": "prov:hadPlan",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "wasInfluencedBy": {
      "@context": {
        "featureType": "@type",
        "entityType": "@type",
        "has_provenance": {
          "@id": "dct:provenance",
          "@type": "@id"
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id"
        },
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "alternateOf": {
          "@id": "prov:alternateOf",
          "@type": "@id"
        },
        "hadPrimarySource": {
          "@id": "prov:hadPrimarySource",
          "@type": "@id"
        },
        "specializationOf": {
          "@id": "prov:specializationOf",
          "@type": "@id"
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id"
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id"
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id"
        },
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "qualifiedGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedGeneration",
          "@type": "@id"
        },
        "qualifiedInvalidation": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id"
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id"
        },
        "qualifiedAttribution": {
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          },
          "@id": "prov:qualifiedAttribution",
          "@type": "@id"
        },
        "provType": "@type",
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "featureType": "@type",
            "entityType": "@type",
            "has_provenance": {
              "@id": "dct:provenance",
              "@type": "@id"
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasDerivedFrom": {
              "@id": "prov:wasDerivedFrom",
              "@type": "@id"
            },
            "alternateOf": {
              "@id": "prov:alternateOf",
              "@type": "@id"
            },
            "hadPrimarySource": {
              "@id": "prov:hadPrimarySource",
              "@type": "@id"
            },
            "specializationOf": {
              "@id": "prov:specializationOf",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "links": {
              "@context": {
                "href": {
                  "@type": "@id",
                  "@id": "oa:hasTarget"
                },
                "rel": {
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  },
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id"
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              },
              "@id": "rdfs:seeAlso"
            },
            "qualifiedGeneration": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedGeneration",
              "@type": "@id"
            },
            "qualifiedInvalidation": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id"
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id"
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id"
            },
            "provType": "@type",
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "entity": {
          "@context": {
            "featureType": "@type",
            "entityType": "@type",
            "has_provenance": {
              "@id": "dct:provenance",
              "@type": "@id"
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasDerivedFrom": {
              "@id": "prov:wasDerivedFrom",
              "@type": "@id"
            },
            "alternateOf": {
              "@id": "prov:alternateOf",
              "@type": "@id"
            },
            "hadPrimarySource": {
              "@id": "prov:hadPrimarySource",
              "@type": "@id"
            },
            "specializationOf": {
              "@id": "prov:specializationOf",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "links": {
              "@context": {
                "href": {
                  "@type": "@id",
                  "@id": "oa:hasTarget"
                },
                "rel": {
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  },
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id"
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              },
              "@id": "rdfs:seeAlso"
            },
            "qualifiedGeneration": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedGeneration",
              "@type": "@id"
            },
            "qualifiedInvalidation": {
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "xsd:dateTime"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id"
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id"
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id"
            },
            "provType": "@type",
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          },
          "@id": "prov:entity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://surroundaustralia.github.io/analytic-transparency/build/annotated/at/activities/derivation/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/surroundaustralia/analytic-transparency](https://github.com/surroundaustralia/analytic-transparency)
* Path: `_sources/activities/derivation`

