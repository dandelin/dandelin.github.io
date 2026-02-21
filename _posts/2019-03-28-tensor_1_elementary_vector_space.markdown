---
layout: post
title: "Tensor #1. Elementary Vector Space"
date: 2019-03-28
description: "Tensor 시리즈 1편: 벡터 스페이스의 기본 정의와 성질"
giscus_comments: true
---

XylyXylyX의 [What is Tensor](https://www.youtube.com/watch?v=_pKxbNyjNe8&list=PLRlVmXqzHjUQARA37r4Qw3SHPqVXgqO6c) 강의를 정리한 노트입니다.

### Vector는 특수한 조건<sub>condition</sub>을 가진 집합입니다.

1. Addition  
   Vector Space $$ \newcommand{\V}{\mathcal{V}} \V $$에 대해서 $$ \newcommand{\and}{\;\&\;} x \in \V \and y \in \V \rightarrow (x + y) \in \V $$
2. Scalar Multiplication  
   $$ \newcommand{\R}{\mathbb{R}} a \in \R, v \in \V \rightarrow ax \in \V $$, 여기서 $$ \R $$은 실수 체<sub>field</sub>이며, 다른 어떠한 필드도 가능합니다. (복소수, 사원수<sub>quaternion</sub>, 팔원수<sub>octonion</sub> 등..)

이 정의에 필수적인 요소들을 모아서 이렇게 씁시다 : $$ \newcommand{\VBa}{(\V, +, \R)} \VBa $$  
각각 집합 $$ \V $$, Addition $$ + $$, Scalar Field (이 경우에는 실수체) $$ \R $$을 의미합니다.

여기서 추가적으로 주의해야 할 것은 $$ \VBa $$의 $$ + $$와 $$ \newcommand{\VBb}{(\mathcal{W}, +, \R)} \VBb $$의 $$ + $$가 다르다는 점입니다. 다시 말해서 $$ w \in \VBa, q \in \VBa $$일 때 $$ w + q $$의 $$ + $$와 $$ r \in \VBb, s \in \VBb $$일 때 $$ r + s $$의 $$ + $$가 같지 않다는 거죠. $$ w + s $$와 같은 $$ + $$는 **정의되지 않았습니다.**

### 벡터는 아래와 같은 성질<sub>property</sub>을 가집니다.

1. Linearity  
   $$ x \in \V, y \in \V, a \in \R \rightarrow ax + ay = a(x+y) \in \V $$
2. Opposite  
   $$ -1 \in \R, x \in \V \rightarrow -x \in \V \and x + (-x) = 0 $$

> Q1. 벡터 스페이스의 종류는 그럼 어떻게 결정되나요?  
> A1. Scalar Field의 종류에 의해 결정됩니다. $$ \R $$이라면 실수 벡터, $$ \mathbb{C} $$라면 복소수 벡터, 이런 식이죠.

> Q2. 만약 두 벡터 스페이스 $$ \VBa $$와 $$ \VBb $$가 있다면, 두 벡터 스페이스는 이름 말고 뭐가 다를 수 있나요?  
> A2. 심볼릭하게는, 다른 점이 없습니다. 아마도 차원<sub>dimension</sub>이 있다면 그들을 구분지을 수 있겠네요.

### 차원이 뭘까요?

$$ q \in \VBa $$를 만들 수 있는 벡터의 최소 집합<sub>minimal set</sub>의 크기를 차원이라고 합니다. $$ q $$가 $$ \VBa $$의 벡터 원소인 $$ w, p, n, o \in \V $$와 스칼라 원소인 $$ a, b, c, d \in \R $$의 결합 $$ q = aw + bp + cn + do $$로 표현되어질 수 있고, 이것보다 더 적은 수의 벡터 원소로는 표현될 수 없다면, $$ \VBa $$의 차원은 4차원이겠네요.

만약 두 벡터 스페이스의 스칼라 필드의 종류가 같고, 차원이 같다면 두 벡터 스페이스는 *Isomorphic*하다고 합니다.

### 기초적인<sub>elementary</sub> 벡터 스페이스

여기까지의 정의로 얻어진 벡터 스페이스를 *Elementary Vector Space*라고 하겠습니다. 우리가 기존에 벡터를 배울 때 같이 따라왔던 내적<sub>inner product</sub>, 데카르트 곱<sub>cartesian product</sub>, 노름<sub>norm</sub>등은 정의되어있지 않습니다. 이러한 성질들이 없어도, 벡터 스페이스는 벡터 스페이스입니다. 이러한 성질들을 추가로 가진 벡터 스페이스들은 *Advanced Vector Space*라고 하겠습니다. 이후에 Tensor Product를 설명하면서 데카르트 곱, Metric Tensor를 설명하면서 내적과 노름이 자연스럽게 정의되게 됩니다.
