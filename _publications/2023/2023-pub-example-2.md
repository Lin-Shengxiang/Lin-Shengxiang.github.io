---
title:          HyperFed:hyperbolic prototypes exploration with consistent aggregation for non-IID data in federated learning
date:           2023-04-14 00:01:00 +0800
selected:       true
pub:            "Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence (IJCAI)"
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-success">Oral</span>'
pub_date:       "2023"
abstract: >-
  Federated learning (FL) collaboratively models user data in a decentralized way. However, in the real world, non-identical and independent data distributions (non-IID) among clients hinder the performance of FL due to three issues, i.e., (1) the class statistics shifting, (2) the insufficient hierarchical information utilization, and (3) the inconsistency in aggregating clients. To address the above issues, we propose HyperFed which contains three main modules, i.e., hyperbolic prototype Tammes initialization (HPTI), hyperbolic prototype learning (HPL), and consistent aggregation (CA). Firstly, HPTI in the server constructs uniformly distributed and fixed class prototypes, and shares them with clients to match class statistics, further guiding consistent feature representation for local clients. Secondly, HPL in each client captures the hierarchical information in local data with the supervision of shared class prototypes in the hyperbolic model space. Additionally, CA in the server mitigates the impact of the inconsistent deviations from clients to server. Extensive studies of four datasets prove that HyperFed is effective in enhancing the performance of FL under the non-IID setting.

cover:          assets/images/covers/hyperfed.png
authors:
  - Xinting Liao
  - Weiming Liu
  - Chaochao Chen†
  - Pengyang Zhou
  - Huabin Zhu
  - Yanchao Tan
  - Jun Wang
  - Yue Qi
links:
  Paper: https://www.ijcai.org/proceedings/2023/440
  Cite: assets/bibtex/liao2023hyperfed.bib
  Code: https://github.com/XeniaLLL/HyperFed_and_FedRANE-master
---
