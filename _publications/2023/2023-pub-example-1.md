---
title:          PPGenCDR:Stable and Robust Framework for Privacy-Preserving Cross-Domain Recommendation
date:           2023-06-26 00:01:00 +0800
selected:       true
pub:            "Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)"
pub_last:       '<span class="badge badge-pill badge-custom badge-secondary">CCF A Conference</span><span class="badge badge-pill badge-custom badge-success">Oral</span>'
pub_date:       "2023"
abstract: >-
  Privacy-preserving cross-domain recommendation (PPCDR) refers to preserving the privacy of users when transferring the knowledge from source domain to target domain for better performance, which is vital for the long-term development of recommender systems. Existing work on cross-domain recommendation (CDR) reaches advanced and satisfying recommendation performance, but mostly neglects preserving privacy. To fill this gap, we propose a privacy-preserving generative cross-domain recommendation (PPGenCDR) framework for PPCDR. PPGenCDR includes two main modules, i.e., stable privacy-preserving generator module, and robust cross-domain recommendation module. Specifically, the former isolates data from different domains with a generative adversarial network (GAN) based model, which stably estimates the distribution of private data in the source domain with ́Renyi differential privacy (RDP) technique. Then the latter aims to robustly leverage the perturbed but effective knowledge from the source domain with the raw data in target domain to improve recommendation performance. Three key modules, i.e., (1) selective privacy preserver, (2) GAN stabilizer, and (3) robustness conductor, guarantee the cost-effective trade-off between utility and privacy, the stability of GAN when using RDP, and the robustness of leveraging transferable knowledge accordingly. The extensive empirical studies on Douban and Amazon datasets demonstrate that PPGenCDR significantly outperforms the state-of-the-art recommendation models while preserving privacy.

cover:          assets/images/covers/ppgencdr.png
authors:
  - Xinting Liao
  - Weiming Liu
  - Xiaolin Zheng
  - Binhui Yao
  - Chaochao Chen†
links:
  Paper: https://ojs.aaai.org/index.php/AAAI/article/view/25566
  Cite: assets/bibtex/liao2023ppgencdr.bib
  Code: https://github.com/XeniaLLL/PPGenCDR
---
