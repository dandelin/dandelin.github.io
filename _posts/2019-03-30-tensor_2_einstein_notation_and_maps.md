---
published: true
layout: single
title: "Tensor #2. Einstien Notation and Maps"
use_math: true
category: "Note"
tags: 
    - "Tensor"
---
XylyXylyX의 [What is Tensor](https://www.youtube.com/watch?v=_pKxbNyjNe8&list=PLRlVmXqzHjUQARA37r4Qw3SHPqVXgqO6c) 강의를 정리한 노트입니다.

## Einstien Notation
[지난 편]({% post_url 2019-03-28-tensor_1_elementary_vector_space %})에서 벡터 스페이스 $\newcommand{\V}{\mathcal{V}} \newcommand{\R}{\mathbb{R}} (\V, +, \R)$와 차원에 대해서 설명했습니다. 차원을 곁들여서 이제 벡터 스페이스를 $\newcommand{\d}{\mathbf{d}} \newcommand{\VBa}[1]{(\V, +, \R, #1)} \newcommand{\VBb}[1]{(\mathcal{W}, +, \R, #1)} \VBa{\d}$라고 쓰겠습니다. $\d$는 벡터 스페이스의 차원을 의미합니다.

$\d = 4$라고 생각하고, 4차원 실수 벡터 공간 $\VBa{4}$를 생각해봅시다[^1]. 그럼 $m \in {\VBa{4}}$은 기저 벡터<sub>basis vector</sub>[^2] $w, v, p, g$와 적절한 스칼라들 $a, b, c, d$의 선형 결합 $m = aw + bv + cp + dg$로 나타낼 수 있을 것입니다.

늘 이런 적당한 알파벳을 찾는 것은 귀찮을 뿐더러 헷갈리기까지 합니다. 따라서 인덱싱<sub>indexing</sub>을 통해서 이 과정을 단순화하고자 합니다. 하나의 벡터를 완전히 표현하는데는 언제나 기저와 적당한 스칼라들의 곱과 합이 필요하기 때문에, 이것을 잘 나타내주는 표현이 필요한데요. 그 표기법을 아인슈타인 표기<sub>Einstein notation</sub>이라고 하겠습니다.

임의의 4차원 벡터 $a$는 아인슈타인 표기로는 $\newcommand{\a}{A^{\mu}e_{\mu}} \a$라고 표기하며, 여기서 $\mu$는 더미 인덱스<sub>dummy index</sub>로, 위 첨자와 아래 첨자에 동시에 등장한다면 반복하며 곱해서 더하라는 뜻을 가집니다. 다시 말해 4차원 벡터일 경우 $\a = \sum_{i}A^ie_i = A^0e_0 + A^1e_1 + A^2e_2 + A^3e_3$입니다.

## Map
두 벡터 스페이스 $\VBa{4}$와 $\VBb{10}$ 사이의 관계를 정의할 수 있을까요? 물론 가능하고, 그걸 우리는 맵<sub>map</sub>이라고 부를 것입니다. 맵은 굉장히 여러 군데에서 쓰여서 그 표기도 다양한데요. 예를 몇 개 들면, $\VBa{4}$에서 $\VBb{10}$로 가는 맵 $\Lambda : \mathcal{V} \rightarrow \mathcal{W}$를 아래와 같이 표현할 수 있습니다.

- operator form: $\Lambda v \rightarrow w$
- function form: $\Lambda(v) \rightarrow w$
- operator와 function 사이 어딘가: $\langle\Lambda, v\rangle \rightarrow w$
  - 이 경우 $\langle\Lambda,\;\rangle$는 operator 처럼 작용하게 됩니다.

앞으로 모든 노트에서는 $\newcommand{\map}[2]{\langle#1,#2\rangle} \map{\;}{\;}$을 사용하게 될 텐데, 그 편리함과 이유는 차차 나오게 됩니다.

그럼 두 벡터 스페이스 $\VBa{4}$와 $\VBb{10}$ 사이의 관계를 정의해볼까요? $\VBa{4}$의 모든 원소를 $\VBb{10}$에 대응시키기 위해선, 기저들의 관계만 정의해주면 됩니다. 왜냐하면 스칼라 필드는 둘 다 공유하고 있기 때문이죠 (실수). $\VBa{4}$의 기저 벡터를 $e_i$라고 하고 $\VBb{10}$의 기저 벡터를 $f_j$라고 한다면. 아래와 같은 꼴로 그 관계를 정의할 수 있을 겁니다.

- $\map{\Lambda}{e_0} = 3f_1 + 2f_4 + f_{10}$
- $\map{\Lambda}{e_1} = \pi f_3 + e^{17}f_0$
- $\map{\Lambda}{e_2} = f_2$
- $\map{\Lambda}{e_3} = f_3 + f_5 + f_7 + f_9$

위의 네 가지 맵핑이 임의로 작성된 것은 충분히 느껴지실 겁니다. 네, 아무렇게나 작성할 수 있습니다. $f_j$의 차수가 1승이기만 한다면요. 이와 같은 맵을 선형 변환<sub>linear map</sub>이라고 합니다. 선형 변환은 아래와 같은 특징을 가집니다. 당연히.. 선형성이죠.

### 선형성<sub>Linearity</sub>
- $\map{\Lambda}{v+p} = \map{\Lambda}{v} + \map{\Lambda}{p}$
- $\map{\Lambda}{av+bp} = a\map{\Lambda}{v} + b\map{\Lambda}{p}$

[지난 편]({% post_url 2019-03-28-tensor_1_elementary_vector_space %})에서 두 벡터 스페이스 $\VBa{4}$와 $\VBb{4}$의 $+$는 서로 다르다고 했고, 두 공간에서 각각 뽑은 벡터 사이의 $+$는 **정의되어 있지 않았다**고 했는데요. 위 식에서 $+$는 그 조건을 잘 만족합니다. 좌변의 $+$는 $\mathcal{V}$의 $+$고, 우변의 $+$는 $\mathcal{W}$의 $+$입니다.

이를 임의의 벡터 $a = \a$에 대해서 적어보면, $\map{\Lambda}{\a} = A^0\map{\Lambda}{e_0} + A^1\map{\Lambda}{e_1} + \ldots$가 될 것입니다. 물론 $\map{\Lambda}{e_i}$는 정의된 후겠죠.

[^1]: 한국어와 영어를 혼용해서 쓸 것입니다. 이해 부탁드립니다. 😅
[^2]: 기저 벡터란 벡터 공간을 생성<sub>span</sub>할 벡터들을 의미합니다, 그저 그 뿐입니다. 이 경우 4차원 공간이니 기저 벡터도 4개겠죠.