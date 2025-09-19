---
title:          FedRANE:Joint Local Relational Augmentation and Global Nash Equilibrium for Federated Learning with Non-IID Data
date:           2023-10-27 00:01:00 +0800
selected:       true
pub:            "Proceedings of the 31st ACM International Conference on Multimedia (MM)"
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-success">Oral</span>'
pub_date:       "2023"
abstract: >-
  FFederated learning (FL) is a distributed machine learning paradigm that needs collaboration between a server and a series of clients with decentralized data. To make FL effective in real-world applications, existing work devotes to improving the modeling of decentralized non-IID data. In non-IID settings, there are intra-client inconsistency that comes from the imbalanced data modeling, and inter-client inconsistency among heterogeneous client distributions, which not only hinders sufficient representation of the minority data, but also brings discrepant model deviations. However, previous work overlooks to tackle the above two coupling inconsistencies together. In this work, we propose FedRANE, which consists of two main modules, i.e., local relational augmentation (LRA) and global Nash equilibrium (GNE), to resolve intra-and inter-client inconsistency simultaneously. Specifically, in each client, LRA mines the similarity relations among different data samples and enhances the minority sample representations with their neighbors using attentive message passing. In server, GNE reaches an agreement among inconsistent and discrepant model deviations from clients to server, which encourages the global model to update in the direction of global optimum without breaking down the clients' optimization toward their local optimums. We conduct extensive experiments on four benchmark datasets to show the superiority of FedRANE in enhancing the performance of FL with non-IID data.

cover:          assets/images/covers/fedrane.png
authors:
  - Xinting Liao
  - Chaochao Chen†
  - Weiming Liu
  - Pengyang Zhou
  - Huabin Zhu
  - Shuheng Shen
  - Weiqiang Wang
  - Mengling Hu
  - Yanchao Tan
  - Xiaolin Zheng
links:
  Paper: https://dl.acm.org/doi/10.1145/3581783.3612178
  Cite: assets/bibtex/liao2023joint.bib
  Code: https://github.com/XeniaLLL/HyperFed_and_FedRANE-master
---


