---
layout: home
title: about
permalink: /
description: Wonjae (Dan) Kim is a multimodal AI researcher and research leader working across representation learning, large-scale embedding, and video search systems.
---

<section class="home-hero" aria-labelledby="home-title">
  <div class="home-hero__copy">
    <p class="home-eyebrow">Wonjae (Dan) Kim <span aria-hidden="true">·</span> 김원재</p>
    <h1 id="home-title">Multimodal intelligence,<br><em>from representations to systems.</em></h1>
    <p class="home-hero__lead">
      I build models and systems that make video searchable, useful, and easier to understand.
    </p>
    <p class="home-hero__body">
      I’m a Lead Research Scientist at
      <a href="https://www.twelvelabs.io">TwelveLabs</a>, where I lead the Embedding & Search team. My work spans
      multimodal foundation models, large-scale retrieval, and the path from research ideas to products people use.
    </p>
    <div class="home-actions" aria-label="Explore Wonjae Kim's work">
      <a class="home-button home-button--primary" href="#research">Explore research</a>
      <a class="home-button" href="#ideas">Read the ideas</a>
      <a class="home-text-link" href="{{ '/cv/' | relative_url }}">View CV <span aria-hidden="true">↗</span></a>
    </div>
    <ul class="home-proof" aria-label="Selected credentials">
      <li>ViLT co-first author</li>
      <li>ICML long talk</li>
      <li>ECCV oral</li>
    </ul>
  </div>

  <figure class="home-portrait">
    <div class="home-portrait__frame">
      <img
        src="{{ '/assets/img/profile/prof_pic5.jpg' | relative_url }}"
        alt="Portrait of Wonjae Kim"
        width="800"
        height="800"
        loading="eager"
        fetchpriority="high"
      >
    </div>
    <figcaption>Researcher <span aria-hidden="true">/</span> builder <span aria-hidden="true">/</span> writer</figcaption>
  </figure>
</section>

<div class="home-trajectory" aria-label="Research trajectory">
  <span>HCI &amp; visualization</span>
  <span class="home-trajectory__arrow" aria-hidden="true">→</span>
  <span>multimodal representation</span>
  <span class="home-trajectory__arrow" aria-hidden="true">→</span>
  <span>video understanding &amp; search</span>
</div>

<section class="home-section" id="research" aria-labelledby="research-title">
  <div class="home-section__heading">
    <div>
      <p class="home-kicker">Selected research</p>
      <h2 id="research-title">Three layers of the work</h2>
    </div>
    <p>
      I’m interested in the full stack of multimodal intelligence: how representations are designed, how data shapes
      them, and how they become reliable systems at scale.
    </p>
  </div>

  <div class="home-research-grid">
    <article class="home-card home-card--research">
      <div class="home-card__topline">
        <span>Architecture</span>
        <span>ICML 2021</span>
      </div>
      <h3><a href="https://proceedings.mlr.press/v139/kim21k.html">ViLT</a></h3>
      <p class="home-card__subtitle">Vision-and-Language Transformer Without Convolution or Region Supervision</p>
      <p>
        A minimal vision-language architecture that removed heavy visual embedders and helped reset the efficiency
        baseline for multimodal learning.
      </p>
      <div class="home-card__footer">
        <span>{{ site.data.citations.papers['UpZ41EwAAAAJ:YsMSGLbcyi4C'].citations }} citations</span>
        <span class="home-card__links">
          <a href="https://proceedings.mlr.press/v139/kim21k.html">Paper</a>
          <a href="https://github.com/dandelin/ViLT">Code</a>
        </span>
      </div>
    </article>

    <article class="home-card home-card--research">
      <div class="home-card__topline">
        <span>Data semantics</span>
        <span>ECCV 2024 oral</span>
      </div>
      <h3><a href="https://arxiv.org/abs/2404.17507">HYPE</a></h3>
      <p class="home-card__subtitle">Hyperbolic Entailment Filtering for Underspecified Images and Texts</p>
      <p>
        A geometric way to identify specificity and entailment in noisy image-text data, making billion-scale
        filtering both more meaningful and more efficient.
      </p>
      <div class="home-card__footer">
        <span>{{ site.data.citations.papers['UpZ41EwAAAAJ:TQgYirikUcIC'].citations }} citations</span>
        <span class="home-card__links">
          <a href="https://arxiv.org/abs/2404.17507">Paper</a>
          <a href="https://github.com/naver-ai/hype">Code</a>
        </span>
      </div>
    </article>

    <article class="home-card home-card--research home-card--systems">
      <div class="home-card__topline">
        <span>Systems</span>
        <span>Now</span>
      </div>
      <h3><a href="https://www.twelvelabs.io">Embedding &amp; Search</a></h3>
      <p class="home-card__subtitle">Multimodal foundation models for video understanding</p>
      <p>
        At TwelveLabs, I lead the team working on joint embedding spaces and large-scale retrieval systems that turn
        research into production search experiences.
      </p>
      <div class="home-card__footer">
        <span>Research → product</span>
        <span class="home-card__links"><a href="https://www.twelvelabs.io">TwelveLabs</a></span>
      </div>
    </article>

  </div>

  <p class="home-section__after">
    <a class="home-text-link" href="{{ '/publications/' | relative_url }}">See all publications <span aria-hidden="true">→</span></a>
  </p>
</section>

<section class="home-section home-section--ideas" id="ideas" aria-labelledby="ideas-title">
  <div class="home-section__heading">
    <div>
      <p class="home-kicker">Ideas &amp; writing</p>
      <h2 id="ideas-title">Frameworks beyond the papers</h2>
    </div>
    <p>
      I write to preserve the context behind an idea, then let readers and agents choose the resolution, language,
      and form they need.
    </p>
  </div>

  <div class="home-ideas-grid">
    <article class="home-idea">
      <p class="home-idea__number" aria-hidden="true">01</p>
      <div>
        <p class="home-card__topline"><span>Reading in the agent era</span><span>2026</span></p>
        <h3>
          <a href="{{ '/blog/2026/Speak-Concisely-Write-Verbosely/' | relative_url }}">Speak Concisely, Write Verbosely</a>
        </h3>
        <p>
          When agents become readers, “omit needless words” stops being a universal rule. Rich source context and
          interactive transformation can coexist.
        </p>
        <a class="home-text-link" href="{{ '/blog/2026/Speak-Concisely-Write-Verbosely/' | relative_url }}">
          Read the essay <span aria-hidden="true">→</span>
        </a>
      </div>
    </article>

    <article class="home-idea">
      <p class="home-idea__number" aria-hidden="true">02</p>
      <div>
        <p class="home-card__topline"><span>Systems &amp; coordination</span><span>2026</span></p>
        <h3>
          <a href="{{ '/blog/2026/Consensus-Reset-Cost-Theory/' | relative_url }}">The Theory of Consensus Reset Cost</a>
        </h3>
        <p>
          A framework for understanding how networks resist monopoly, and why the cost of rewriting consensus changes
          across physical, institutional, and digital assets.
        </p>
        <a class="home-text-link" href="{{ '/blog/2026/Consensus-Reset-Cost-Theory/' | relative_url }}">
          Read the essay <span aria-hidden="true">→</span>
        </a>
      </div>
    </article>

  </div>

  <p class="home-section__after">
    <a class="home-text-link" href="{{ '/blog/' | relative_url }}">Browse all notes and essays <span aria-hidden="true">→</span></a>
  </p>
</section>

<section class="home-now" aria-labelledby="now-title">
  <div class="home-now__copy">
    <p class="home-kicker">Now</p>
    <h2 id="now-title">Building the search layer for video-native AI.</h2>
    <p>
      At TwelveLabs, we’re working on the representation and retrieval problems that sit between long-form video and
      useful intelligence: joint embedding spaces, semantic structure, and search that holds up at production scale.
    </p>
  </div>
  <aside class="home-now__aside" aria-label="Join the team">
    <p class="home-now__label">Join the team · Seoul</p>
    <p>We’re looking for scientists and engineers who want to move video-language research from idea to production.</p>
    <div>
      <a class="home-button home-button--light" href="https://jobs.ashbyhq.com/twelve-labs/38e8e1c9-bf91-449c-b64a-c3f481099801">Open role</a>
      <a class="home-text-link home-text-link--light" href="https://calendar.app.google/RFWg71Zb3GED9nkeA">Coffee chat <span aria-hidden="true">↗</span></a>
    </div>
  </aside>
</section>

<section class="home-contact" aria-labelledby="contact-title">
  <div>
    <p class="home-kicker">Elsewhere</p>
    <h2 id="contact-title">Research, code, and ongoing notes.</h2>
  </div>
  <div class="home-contact__links">
    <a href="https://scholar.google.com/citations?user=UpZ41EwAAAAJ">Google Scholar <span aria-hidden="true">↗</span></a>
    <a href="https://github.com/dandelin">GitHub <span aria-hidden="true">↗</span></a>
    <a href="https://www.linkedin.com/in/wjk">LinkedIn <span aria-hidden="true">↗</span></a>
    <a href="mailto:contact@wonjae.kim">Email <span aria-hidden="true">↗</span></a>
  </div>
</section>
