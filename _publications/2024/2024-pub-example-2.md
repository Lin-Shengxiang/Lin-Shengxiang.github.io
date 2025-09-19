---
title:          FOOGD:Federated Collaboration for Both Out-of-distribution Generalization and Detection
date:           2024-12-09 00:01:00 +0800
selected:       true
pub:            "Advances in Neural Information Processing Systems"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-warning">Poster</span>'
pub_date:       "2024"

abstract: >-
  Federated learning (FL) is a promising machine learning paradigm that collaborates with client models to capture global knowledge. However, deploying FL models in real-world scenarios remains unreliable due to the coexistence of in-distribution data and unexpected out-of-distribution (OOD) data, such as covariate-shift and semantic-shift data. Current FL researches typically address either covariate-shift data through OOD generalization or semantic-shift data via OOD detection, overlooking the simultaneous occurrence of various OOD shifts. In this work, we propose FOOGD, a method that estimates the probability density of each client and obtains reliable global distribution as guidance for the subsequent FL process. Firstly, SM3D in FOOGD estimates score model for arbitrary distributions without prior constraints, and detects semantic-shift data powerfully. Then SAG in FOOGD provides invariant yet diverse knowledge for both local covariate-shift generalization and client performance generalization. In empirical validations, FOOGD significantly enjoys three main advantages: (1) reliably estimating non-normalized decentralized distributions, (2) detecting semantic shift data via score values, and (3) generalizing to covariate-shift data by regularizing feature extractor. The prejoct is open in <a href="https://github.com/XeniaLLL/FOOGD-main">🔗Github</a>.
  
cover:          assets/images/covers/foogd.png
authors:
  - Xinting Liao
  - Weiming Liu
  - Pengyang Zhou
  - Fengyuan Yu
  - Jiahe Xu
  - Jun Wang
  - Wenjie Wang
  - Chaochao Chen
  - Xiaolin Zheng†
links:
  Code: https://github.com/XeniaLLL/FOOGD-main
  Paper: https://nips.cc/virtual/2024/poster/96103
#  Poster: assets/images/poster/icml2024-ws.jpeg
  Cite: assets/bibtex/liao2024foogd.bib
---
