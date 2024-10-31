call sda db create -n geotest -o spatial.enabled=true
REM query.describe.strategy=bidirectional
REM graphql.auto.schema
REM graphql.auto.schema.source=shacl
REM auto.schema.reasoning
REM reasoning.sameas (ON,OFF, FULL)
REM tag:stardog:api:context:schema
REM reasoning.schemas prov=https://www.w3.org/ns/prov
REM reasoning.schemas.graphs https://www.w3.org/ns/prov, tag:stardog:api:context:schema
call sd data add -- --named-graph https://www.w3.org/ns/prov prov-o.ttl

call sd reasoning schema --add prov --graphs https://www.w3.org/ns/prov

call sd namespace add --prefix prov --uri "https://www.w3.org/ns/prov"
REM call sd data model  --named-graph https://www.w3.org/ns/prov prov-o.ttl
