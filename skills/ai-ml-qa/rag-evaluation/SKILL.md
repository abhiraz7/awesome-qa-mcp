---
name: rag-evaluation
description: design and analyze evaluations for retrieval-augmented generation systems, including retrieval quality, grounding, answer relevance and failure attribution.
---

# rag evaluation

help evaluate a retrieval-augmented generation system as a pipeline. assess retrieval and generation separately as well as the end-to-end answer.

## workflow

1. define user tasks, corpus scope, expected answer behaviour and impact of errors.
2. build representative questions, including answerable, unanswerable, ambiguous and multi-hop cases.
3. establish reference answers or expected evidence where feasible.
4. inspect retrieved chunks for relevance, coverage, ranking, freshness and access control.
5. assess generated answers for correctness, relevance, completeness, grounding and appropriate abstention.
6. test citations or source references for support: cited material should substantiate the claim.
7. investigate failures across ingestion, parsing, chunking, embedding, retrieval, reranking, context assembly and generation.
8. compare changes using the same evaluation set and document metric limitations.

## evaluation dimensions

consider retrieval precision and recall, context relevance, answer correctness, faithfulness or groundedness, citation quality, abstention behaviour, latency and cost. select metrics that match the product and available labels; no single metric is a complete measure of quality.

## failure cases

include missing documents, stale content, conflicting sources, duplicate passages, noisy retrieval, prompt injection in retrieved content, permission-restricted documents and questions outside the corpus.

## boundaries

do not invent a gold answer or evaluation score. explain dataset coverage and bias. do not claim a system is grounded solely because it returns citations; verify whether the cited evidence supports the answer.
