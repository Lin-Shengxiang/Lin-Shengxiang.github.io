---
title:          Rethinking the Representation in Federated Unsupervised Learning with Non-IID Data
date:           2024-06-18 00:01:00 +0800
selected:       true
pub:            "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-warning">Poster</span>'
pub_date:       "2024"

abstract: >-
  Federated learning achieves effective performance in modeling decentralized data. In practice client data are not well-labeled which makes it potential for federated unsupervised learning (FUSL) with non-IID data. However the performance of existing FUSL methods suffers from insufficient representations i.e. (1) representation collapse entanglement among local and global models and (2) inconsistent representation spaces among local models. The former indicates that representation collapse in local model will subsequently impact the global model and other local models. The latter means that clients model data representation with inconsistent parameters due to the deficiency of supervision signals. In this work we propose FedU2 which enhances generating uniform and unified representation in FUSL with non-IID data. Specifically FedU2 consists of flexible uniform regularizer (FUR) and efficient unified aggregator (EUA). FUR in each client avoids representation collapse via dispersing samples uniformly and EUA in server promotes unified representation by constraining consistent client model updating. To extensively validate the performance of FedU2 we conduct both cross-device and cross-silo evaluation experiments on two benchmark datasets i.e. CIFAR10 and CIFAR100.
  
cover:          assets/images/covers/fedu2.png
authors:
  - Xinting Liao
  - Weiming Liu
  - Chaochao Chen†
  - Pengyang Zhou
  - Fengyuan Yu
  - Huabin Zhu
  - Binhui Yao
  - Tao Wang
  - Xiaolin Zheng
  - Yanchao Tan
links:
  Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Liao_Rethinking_the_Representation_in_Federated_Unsupervised_Learning_with_Non-IID_Data_CVPR_2024_paper.html
#  Poster: assets/images/poster/icml2024-ws.jpeg
  Cite: assets/bibtex/liao2024rethinking.bib
  Code: https://github.com/XeniaLLL/FedU2
---


