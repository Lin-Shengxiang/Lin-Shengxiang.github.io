---
title:          FOCoOp: Enhancing Out-of-Distribution Robustness in Federated Prompt Learning for Vision-Language Models
date:           2025-07-12 00:01:00 +0800
selected:       true
pub:            "Forty-Second International Conference on Machine Learning"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-warning">Poster</span>'
pub_date:       "2025"

abstract: >-
    Federated prompt learning (FPL) for vision-language models is a powerful approach to collaboratively adapt models across distributed clients while preserving data privacy. However, existing FPL approaches suffer from a trade-off between performance and robustness, particularly in out-of-distribution (OOD) shifts, limiting their reliability in real-world scenarios. The inherent in-distribution (ID) data heterogeneity among different clients makes it more challenging to maintain this trade-off. To fill this gap, we introduce a Federated OOD-aware Context Optimization (FOCoOp) framework, which captures diverse distributions among clients using ID global prompts, local prompts, and OOD prompts. Specifically, FOCoOp leverages three sets of prompts to create both class-level and distribution-level separations, which adapt to OOD shifts through bi-level distributionally robust optimization. Additionally, FOCoOp improves the discrimination consistency among clients, i.e., calibrating global prompts, seemingly OOD prompts, and OOD prompts by semi-unbalanced optimal transport. The extensive experiments on real-world datasets demonstrate that FOCoOp effectively captures decentralized heterogeneous distributions and enhances robustness of different OOD shifts. The project is available at GitHub.  

cover:          assets/images/covers/focoop.png
authors:
  - Xinting Liao*
  - Weiming Liu*
  - Jiaming Qian
  - Pengyang Zhou
  - Jiahe Xu
  - Wenjie Wang
  - Chaochao Chen
  - Xiaolin Zheng†
  - Tat-Seng Chua
  
links:
  Code: https://github.com/PengyangZhou/FOCoOp.git
  Paper: https://openreview.net/forum?id=XCLZgbm99O
#  Poster: assets/images/poster/icml2024-ws.jpeg
  Cite: assets/bibtex/liao2025focoop.bib
---
