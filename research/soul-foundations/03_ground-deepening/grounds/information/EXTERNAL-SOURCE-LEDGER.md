# Information / Representation State — External Source Ledger

**Status:** active node source ledger; N1/N2 sources captured  
**Date:** 2026-09-04

This ledger records why each external source was used. It does not make any source taxonomy authoritative for SOUL Foundations.

| Source | Tradition / role | Decision-relevant use |
|---|---|---|
| Kaelbling, Littman & Cassandra (1998), *Planning and acting in partially observable stochastic domains*, DOI `10.1016/S0004-3702(98)00023-X` | decision/control theory | independent separation of underlying state, observation and belief/state estimate |
| Kaelbling, POMDP state-estimator discussion, https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a-html/node56.html | control/agent modelling | accessible explanation of belief state as estimate over environment states from observations/history |
| Cassandra et al. POMDP retrospective, https://cassandra.org/arc/talks/aaai2013/index.html | control/agent modelling | action/observation/belief distinctions; observation may inform without directly changing state |
| OGC Timeseries Profile of Observations & Measurements, https://docs.ogc.org/is/15-043r3/15-043r3.html | measurement / observation standards | distinguishes feature/property of interest, observation act/procedure and result estimate; supports actual-vs-observed/result boundary |
| W3C PROV-DM, https://www.w3.org/TR/prov-dm/ | provenance / data modelling | provenance as structured relations among entities, activities and agents; warns against treating provenance as simple information subtype |
| W3C PROV Constraints, https://www.w3.org/TR/prov-constraints/ | provenance / consistency | temporal/identity/derivation constraints; provenance information has its own validity structure |
| Stanford Encyclopedia of Philosophy, *Evidence*, https://plato.stanford.edu/entries/evidence/ | epistemology | evidence is relational to justification/target proposition/hypothesis; supports role/relation treatment |
| Stanford Encyclopedia of Philosophy, *Mental Representation*, https://plato.stanford.edu/entries/mental-representation/ | philosophy of mind / cognitive representation | representation is not equivalent to causal information; attitudes can differ while content relation is shared |
| Claude Shannon (1948), *A Mathematical Theory of Communication* | information theory | falsifier for overbroad `Information` label: engineering information can abstract away semantics |
| Stanford Encyclopedia of Philosophy, *Semantic Conceptions of Information*, https://plato.stanford.edu/entries/information-semantic/ | philosophy of information | documents multiple semantic/informational conceptions; supports label polysemy warning |
| Anind K. Dey (2001), *Understanding and Using Context*, https://kilthub.cmu.edu/articles/journal_contribution/Understanding_and_Using_Context/6470603 | HCI / context-aware computing | context as use/entity-relative information; supports treating context cautiously as relation/view rather than intrinsic category |
| Wang & Strong (1996), *Beyond Accuracy: What Data Quality Means to Data Consumers*, https://www.jmis-web.org/articles/1002 | information systems / data quality | independent quality dimensions are stakeholder/task/system views; useful anti-taxonomy falsifier |
| ISO/IEC 25012:2008, https://www.iso.org/standard/35736.html | data quality standard | data quality characteristics vary by stakeholder and include inherent/system-dependent perspectives; quality dimensions are not automatically ontology branches |
| Wilkinson et al. (2016), *FAIR Guiding Principles*, https://doi.org/10.1038/sdata.2016.18 | scientific data stewardship | findability/accessibility/interoperability/reusability are use/stewardship desiderata crossing informational objects, metadata and infrastructure; anti-collapse evidence |
| NIST FAIR summary, https://www.nist.gov/itl/ssd/information-systems-group/configurable-data-curation-system-cdcs/cdcs-help-and-resources-1 | scientific data stewardship | current public restatement of FAIR dimensions and provenance/identifier/access relations |

## Source-use rule

Use these sources for structural falsification and problem discovery only within the claims they support.

Do not:

- import POMDP probability structure as universal epistemology;
- import O&M classes as SOUL classes;
- import PROV as final relation schema;
- import philosophical evidence theories as one mandatory evidential calculus;
- import data-quality or FAIR dimensions as Information children;
- infer architecture or implementation choices from any source above.
