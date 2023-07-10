from pyshacl import validate

shapes_file = '''\
# prefix: ex
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix schema: <http://schema.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.aalto.fi#> .
@prefix dicp: <https://w3id.org/digitalconstruction/0.5/Processes#> .
@prefix dice: <https://w3id.org/digitalconstruction/0.5/Entities#> .
@prefix dicv: <https://w3id.org/digitalconstruction/0.5/Variables#> .
@prefix dica: <https://w3id.org/digitalconstruction/0.5/Agents#> .
@prefix dicm: <https://w3id.org/digitalconstruction/0.5/Materials#> .
@prefix dicr: <https://w3id.org/digitalconstruction/0.5/Rules#> .

ex:DrywallStageRuleShape a sh:NodeShape,rdfs:Class;
sh:targetClass dicp:Activity;
 sh:sparql [
        a sh:SPARQLConstraint ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:message "the activity is at Not started stage from the image." ;
        sh:select """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            SELECT $this
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
FILTER (?framevisibilityvalue ="False" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:sparql [
        a sh:SPARQLConstraint ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:message "the activity is at Wiring stage from the image." ;
        sh:select """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            SELECT $this
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="True"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:sparql [
        a sh:SPARQLConstraint ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:message "the activity is at Back Panelling stage from the image." ;
        sh:select """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            SELECT $this
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="True"&& ?backpanelvisibilityvalue = "True" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:sparql [
        a sh:SPARQLConstraint ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:message "the activity is at front panelling stage from the image." ;
        sh:select """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            SELECT $this
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
FILTER (?framevisibilityvalue ="False" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="True") .
            }
            """
];
sh:sparql [
        a sh:SPARQLConstraint ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:message "the activity is at Framing stage from the image." ;
        sh:select """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            SELECT $this
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:construct """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            CONSTRUCT {$this dicv:hasProperty ex:Stage.
              ex:Stage dicv:hasPropertyState _:v .
              _:v dicv:hasValue "Not started".
              _:v dicv:hasCreationTime ?time.
                      }
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
                ?image dici:isAbout ?framevisibilitystate .
                ?image dici:isCreatedAt ?time .
FILTER (?framevisibilityvalue ="False" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:construct """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            CONSTRUCT {$this dicv:hasProperty ex:Stage.
              ex:Stage dicv:hasPropertyState _:v .
              _:v dicv:hasValue "Wiring".
              _:v dicv:hasCreationTime ?time.
                      }
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
                ?image dici:isAbout ?framevisibilitystate .
                ?image dici:isCreatedAt ?time .
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="True"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:construct """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            CONSTRUCT {$this dicv:hasProperty ex:Stage.
              ex:Stage dicv:hasPropertyState _:v .
              _:v dicv:hasValue "BackPaneling".
              _:v dicv:hasCreationTime ?time.
                      }
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
                ?image dici:isAbout ?framevisibilitystate .
                ?image dici:isCreatedAt ?time .
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="True"&& ?backpanelvisibilityvalue = "True" && ?frontpanelvisibilityvalue ="False") .
            }
            """
];
 sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:construct """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            CONSTRUCT {$this dicv:hasProperty ex:Stage.
                          ex:Stage dicv:hasPropertyState _:v .
                          _:v dicv:hasValue "FrontPaneling".
                          _:v dicv:hasCreationTime ?time.
                      }
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
                ?image dici:isAbout ?framevisibilitystate .
                ?image dici:isCreatedAt ?time .
FILTER (?framevisibilityvalue ="False" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="True") .
            }
            """
];
sh:rule [
        a sh:SPARQLRule ;
        sh:prefixes ex: ;
        sh:prefixes dicp: ;
        sh:prefixes dice: ;
        sh:prefixes rdfs: ;
        sh:prefixes dicv: ;
        sh:construct """
            PREFIX ex: <http://example.aalto.fi#>
            PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
            PREFIX sh: <http://www.w3.org/ns/shacl#>
            PREFIX sosa: <http://www.w3.org/ns/sosa/>
            PREFIX bot: <https://w3id.org/bot#>
            CONSTRUCT {$this dicv:hasProperty ex:Stage.
                          ex:Stage dicv:hasPropertyState _:v .
                          _:v dicv:hasValue "Framing".
                          _:v dicv:hasCreationTime ?time.
                      }
            WHERE {
                $this a dicp:Activity .
                $this dicp:hasObject ?drywall  .
                ?drywall  dice:hasMemberpart ?frame .
                ?frame a  dice:DrywallFrame .
                ?frame dicv:hasProperty  ?framevisibility .
                ?framevisibility a dicv:Property.
                ?framevisibility dicv:hasPropertyState ?framevisibilitystate.
                ?framevisibilitystate a dicv:PropertyState.
                ?framevisibilitystate dicv:hasValue ?framevisibilityvalue.
                ?drywall  dice:hasMemberpart ?wire .
                ?wire a  dice:DrywallWire .
                ?wire dicv:hasProperty  ?wirevisibility .
                ?wirevisibility a dicv:Property.
                ?wirevisibility dicv:hasPropertyState ?wirevisibilitystate.
                ?wirevisibilitystate a dicv:PropertyState.
                ?wirevisibilitystate dicv:hasValue ?wirevisibilityvalue.
                ?drywall  dice:hasMemberpart ?backpanel .
                ?backpanel a  dice:DrywallBackpanel .
                ?backpanel dicv:hasProperty  ?backpanelvisibility .
                ?backpanelvisibility a dicv:Property.
                ?backpanelvisibility dicv:hasPropertyState ?backpanelvisibilitystate.
                ?backpanelvisibilitystate a dicv:PropertyState.
                ?backpanelvisibilitystate dicv:hasValue ?backpanelvisibilityvalue.
                ?drywall  dice:hasMemberpart ?frontpanel .
                ?frontpanel a  dice:DrywallFrontpanel .
                ?frontpanel dicv:hasProperty  ?frontpanelvisibility .
                ?frontpanelvisibility a dicv:Property.
                ?frontpanelvisibility dicv:hasPropertyState ?frontpanelvisibilitystate.
                ?frontpanelvisibilitystate a dicv:PropertyState.
                ?frontpanelvisibilitystate dicv:hasValue ?frontpanelvisibilityvalue.
                ?image dici:isAbout ?framevisibilitystate .
                ?image dici:isCreatedAt ?time .
FILTER (?framevisibilityvalue ="True" && ?wirevisibilityvalue="False"&& ?backpanelvisibilityvalue = "False" && ?frontpanelvisibilityvalue ="False") .
            }
            """
].

'''
shapes_file_format = 'turtle'

data_file = '''
# prefix: ex
@prefix dicv: <https://w3id.org/digitalconstruction/0.5/Variables#> .
@prefix dici: <https://w3id.org/digitalconstruction/0.5/Information#> .
@prefix dice: <https://w3id.org/digitalconstruction/0.5/Entities#> .
@prefix dicp: <https://w3id.org/digitalconstruction/0.5/Processes#> .


<example.aalto.fi/Apartment/2d> a dice:Location ;
    dice:isLocationOf <example.aalto.fi/Wall/2d/d1>,
        <example.aalto.fi/Wall/2d/d2>,
        <example.aalto.fi/Wall/2d/d3>,
        <example.aalto.fi/Wall/2d/d4>,
        <example.aalto.fi/Wall/2d/d5>,
        <example.aalto.fi/Wall/2d/d6>,
        <example.aalto.fi/Wall/2d/d7>,
        <example.aalto.fi/Wall/2d/d8> .

<example.aalto.fi/DrywallInstallation/2d/d1> a dicp:Activity;
dicp:hasObject <example.aalto.fi/Wall/2d/d1>  .

<example.aalto.fi/Wall/2d/d1> a dice:BuildingObject ;
    dice:hasMemberpart <example.aalto.fi/BackPanel/2d/d1>,
        <example.aalto.fi/Frame/2d/d1>,
        <example.aalto.fi/FrontPanel/2d/d1>,
        <example.aalto.fi/Wire/2d/d1> .


<example.aalto.fi/BackPanel/2d/d1> a dice:DrywallBackpanel ;
    dicv:hasProperty <example.aalto.fi/BackPanelVisibility/2d/d1> .

<example.aalto.fi/FrontPanel/2d/d1> a dice:DrywallFrontpanel ;
    dicv:hasProperty <example.aalto.fi/FrontPanelVisibility/2d/d1> .

<example.aalto.fi/Frame/2d/d1> a dice:DrywallFrame  ;
    dicv:hasProperty <example.aalto.fi/FrameVisibility/2d/d1> .

<example.aalto.fi/Wire/2d/d1> a dice:DrywallWire ;
    dicv:hasProperty <example.aalto.fi/WireVisibility/2d/d1> .

<example.aalto.fi/Image_20210303_2d_d1> a dici:Image ;
    dici:isAbout <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210303> .

<example.aalto.fi/BackPanelVisibility/2d/d1> a dicv:Property ;
    dicv:hasPropertyState <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210310>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210318>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210324>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210331>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210406>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210413>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210421>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210428>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210504>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210511>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210518>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210526>,
        <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210716> .

<example.aalto.fi/FrameVisibility/2d/d1> a dicv:Property ;
    dicv:hasPropertyState <example.aalto.fi/FrameVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210310>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210318>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210324>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210331>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210406>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210413>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210421>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210428>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210504>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210511>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210518>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210526>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210716> .

<example.aalto.fi/FrontPanelVisibility/2d/d1> a dicv:Property ;
    dicv:hasPropertyState <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210310>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210318>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210324>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210331>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210406>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210413>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210421>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210428>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210504>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210511>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210518>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210526>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210716> .

<example.aalto.fi/WireVisibility/2d/d1> a dicv:Property ;
    dicv:hasPropertyState <example.aalto.fi/WireVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210310>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210318>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210324>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210331>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210406>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210413>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210421>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210428>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210504>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210511>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210518>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210526>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210716> .

<example.aalto.fi/BackPanelVisibilityState/2d/d1_20210303> a dicv:PropertyState ;
    dicv:hasTimeOfCreation "20210303" ;
    dicv:hasValue "False" .

<example.aalto.fi/FrameVisibilityState/2d/d1_20210303> a dicv:PropertyState ;
    dicv:hasTimeOfCreation "20210303" ;
    dicv:hasValue "False" .

<example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210303> a dicv:PropertyState ;
    dicv:hasTimeOfCreation "20210303" ;
    dicv:hasValue "False" .

<example.aalto.fi/WireVisibilityState/2d/d1_20210303> a dicv:PropertyState ;
    dicv:hasTimeOfCreation "20210303" ;
    dicv:hasValue "False" .

<example.aalto.fi/Image_20210303_2d_d1> a dici:Image ;
    dici:isAbout <example.aalto.fi/BackPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrameVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/FrontPanelVisibilityState/2d/d1_20210303>,
        <example.aalto.fi/WireVisibilityState/2d/d1_20210303> ;
    dici:isCreatedAt "20210303" .



'''
data_file_format = 'turtle'

conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format, inference='rdfs',
                                     serialize_report_graph=True, advanced=True)

print(conforms)
print(v_graph)
print(v_text)
