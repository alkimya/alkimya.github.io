---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 1.0.4
    jupytext_version: 1.16.2
kernelspec:
  display_name: Python 3.11.2 64-bit
  name: python3
---

# Ensembles et fonctions

## Ensembles

:::{prf:definition} Ensemble par extension ou par compréhension
Un ensemble peut être défini par **extension**, en énumérant tous ses éléments.  
Un ensemble peut être défini par **compréhension**, par une proposition caractérisant ses éléments.
:::

:::{prf:remark}
Un ensemble n'est pas ordonné (_ex :_ $\{x, y\} = \{y, x\}$).  
Les éléments d'un ensemble ne sont pas dupliqués, ils sont tous distincts ( _ex :_ $\{x, y, y, y, x\} = \{x, y\}$).  
L'ensemble vide $\varnothing$ ne contient aucun élément : $\: \forall x, x \notin \varnothing$, cet ensemble est unique.  
Un ensemble à un élément est appelé un singleton.
:::

### Sous-ensemble

:::{prf:definition} Sous-ensemble - Inclusion
Soient $E$ et $F$ des ensembles, $F$ est un **sous-ensemble ou partie** de $E$, si $x \in F \implies x \in E$  
Le sous-ensemble $F$ est **inclus** dans $E$ et se note $F \subseteq E$.
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10' : 1, '01' : 0, '11' : 1}, set_labels=('E', 'F'), set_colors=('b', 'r'))

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('$F \subseteq E$')

plt.title("Sous-ensemble F inclus dans E")
plt.show()
```

Nous avons alors une nouvelle caractérisation de l'égalité de deux ensembles.

:::{prf:proposition} Égalité de deux ensembles
Soient $E$ et $F$ des ensembles, $E$ et $F$ sont égaux, si et seulement si  
$E = F \iff (F \subseteq E) \land (E \subseteq F)$ soit $x \in F \iff x \in E$
:::

:::{prf:proposition} Transitivité de l'inclusion
Soient $E$, $F$ et $G$ des ensembles alors  $(F \subseteq G \: \land \: G \subseteq E) \implies F \subseteq E$
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

v = venn3(subsets={'100': 1, '010': 0, '110': 1, '001': 0, '101': 0, '011': 0, '111': 1}, set_labels=('E', 'G', 'F'), set_colors=('b', 'r', 'g'))

v.get_label_by_id('100').set_text('')
v.get_label_by_id('110').set_text('$G \subseteq E$')
v.get_label_by_id('111').set_text('\t\t$F \subseteq G$')

plt.title("Transitivité de l'inclusion")
plt.show()
```

### Ensemble des parties d'un ensemble

:::{prf:definition} Ensemble des parties d'un ensemble
Soit $E$ un ensemble.  
L'**ensemble des parties** de $E$ est l'ensemble de tous les sous-ensembles de $E$, il se note $\mathcal{P}(E)$.  
$\mathcal{P}(E) = \{F | F \subseteq E\}$
:::

:::{prf:proposition} Caractéristiques de $\mathcal{P}(E)$
Soit $E$ un ensemble.  
$\varnothing \in \mathcal{P}(E)$ et $E \in \mathcal{P}(E)$  
$\mathcal{P}(E)$ n'est jamais vide.
:::

:::{prf:example}
$\mathcal{P}(\varnothing) = \{\varnothing\}$, c'est le singleton qui contient l'ensemble vide (lui-même ne contenant rien).  
$\mathcal{P}(\{\varnothing\}) = \{\varnothing, \{\varnothing\}\}$  
$\mathcal{P}(\{0, 1\}) = \{\varnothing, \{0\}, \{1\}, \{0, 1\}\}$
:::

### Opération sur les ensembles

:::{prf:definition} Complémentaire d'un ensemble
Soient $E$ un ensemble, $F$ un sous-ensemble de $E$.  
Le **complémentaire** de $F$ dans $E$ est l'ensemble des $x$ appartenant à $E$ mais pas à $F$, il se note $\overline{F}$, parfois $\complement_E F$ ou $F^c$  
$\overline{F} = \{x | x \in E \lor x \notin F\}$
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 0, '11': 1}, set_labels=('E', 'F'), set_colors=('b', 'r'))

v.get_label_by_id('11').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('10').set_text('$\overline{F}$')

plt.title("Complémentaire de F dans E")
plt.show()
```

:::{prf:definition} Union d'ensembles
Soient $E$ et $F$ des ensembles.  
L'**union** de $E$ et $F$ est l'ensemble des $x$ appartenant à $E$ ou à $F$, il se note $E \cup F$ et se lit $E$ union $F$.  
$E \cup F = \{x | x \in E \: \lor \: x \in F\}$
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels=('E', 'F'), set_colors=('b', 'b'))

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('$E \cup F$')

plt.title("Union de E et F\n$E \cup F$")
plt.show()
```

:::{prf:definition} Intersection d'ensembles
Soient $E$ et $F$ des ensembles.  
L'**intersection** de $E$ et $F$ est l'ensemble des $x$ appartenant à $E$ et à $F$, il se note $E \cap F$ et se lit $E$ intersection $F$ ou $E$ inter $F$.  
$E \cap F = \{x | x \in E \: \land \: x \in F\}$
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels=('E', 'F'), set_colors=('b', 'r'))

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('$E \cap F$')

plt.title("Intersection de E et F\n$E \cap F$")
plt.show()
```

:::{prf:proposition} Propriétés de l'union et de l'intersection
Soient $E$, $F$ et $G$ des ensembles.

L'union de $E$ et de $F$ est le plus petit ensemble contenant à la fois $E$ et $F$, c'est à dire  

- $E \subseteq (E \cup F)$ et $F \subseteq (E \cup F)$ et  
- $(F \subseteq E) \land (G \subseteq E) \implies (F \cup G) \subseteq E$

L'intersection de $E$ et de $F$ est le plus grand ensemble contenu à la fois dans $E$ et dans $F$, c'est à dire  

- $(E \cap F) \subseteq E$ et $(E \cap F) \subseteq F$ et  
- $(G \subseteq E) \land (G \subseteq F) \implies G \subseteq (E \cap F)$

Si $F \subseteq E$, $E \cup F = E$ et $E \cap F = F$.

**commutativité :** $\quad E \cup F = F \cup E\:$ et $\: E \cap F = F \cap E$

**associativité :** $\quad (E \cup F) \cup G = E \cup (F \cup G) \:$ et $\: (E \cap F) \cap G = E \cap (F \cap G)$

**distributivité :** L'union et l'intersection sont distributives l'une par rapport à l'autre.  
$(E \cup F) \cap G = (E \cap G) \cup (F \cap G)$  
$(E \cap F) \cup G = (E \cup G) \cap (F \cup G)$

**lois de Morgan :** $\quad \overline{E \cup F} = \overline{E} \cap \overline{F} \:$ et $\: \overline{E \cap F} = \overline{E} \cup \overline{F}$
:::

:::{prf:definition} Ensembles disjoints
Soient $E$ et $F$ des ensembles.  
$E$ et $F$ sont **disjoints** si $E \cap F = \varnothing$  
$E \cup F$ est alors une **union disjointe** de $E$ et $F$ et se note $E \sqcup F$.
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 1, '11': 0}, set_labels=('E', 'F'), set_colors=('b', 'r'))

v.get_label_by_id('10').set_text('$E$')
v.get_label_by_id('01').set_text('$F$')

plt.title("Ensembles disjoints\n$E \sqcup F$")
plt.show()
```

:::{prf:definition} Différence d'ensembles
Soient $E$ et $F$ des ensembles.  
La **différence** de $F$ dans $E$ est l'ensemble des $x$ appartenant à $E$ mais pas à $F$, il se note $E \setminus F$ et se lit $E$ moins $F$.  
$E \setminus F = \{x | x \in E \: \land \: x \notin F\}$

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels=('E', 'F'), set_colors=('b', 'r'))

v.get_label_by_id('10').set_text('$E \setminus F$')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('')

plt.title("Différence d'ensembles\n$E \setminus F$")
plt.show()
```

Dans le cas où $F$ est un sous-ensemble de $E$, la différence de $F$ dans $E$ est le complémentaire de $F$ dans $E$.  
$F \subseteq E \: \iff \: E \backslash F = \overline{F}$
:::

:::{prf:definition} Différence symétrique d'ensembles
Soient $E$ et $F$ des ensembles.  
La **différence symétrique** de $E$ et $F$ est l'ensemble des $x$ appartenant à $E$ ou à $F$ mais pas à l'autre, il se note $E \Delta F$ et se lit $E$ delta $F$.  
$\begin{split}
E \Delta F &= (E \cup F) \backslash (E \cap F) \\
&= (E \backslash F) \cup (F \backslash E) \\
&= \{x | (x \in E \backslash F) \lor (x \in F \backslash E))\}
\end{split}$
:::

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

v = venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels=('E', 'F'), set_colors=('b', 'b'))

v.get_patch_by_id('11').set_color('w')

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('')

plt.title("Différence symétrique de E et F\n$E \Delta F$")
plt.show()
```

### Produit cartésien

:::{prf:definition} Produit cartésien de deux ensembles $E$ et $F$
Soient $E$ et $F$ des ensembles non vides.  
Le **produit cartésien** de $E$ et $F$ est l'ensemble des couples $(x, y)$ tels que $x$ appartient à $E$ et $y$ appartient à $F$, il se note $E \times F$ et se lit $E$ croix $F$ ou $E$ par $F$.  
$E \times F = \{x, y | x \in E \land y \in F\}$  
Lorsque $E = F$, $E \times E$ se note $E^2$.
:::

:::{prf:example} Jeu de cartes
Nous pouvons modéliser un jeu de cartes comme un ensemble $P$ produit cartésien de l'ensemble couleurs $C =\{C{oe}ur, Trèfle, Carreau, Pique\}$ avec l'ensemble valeurs $V = \{As, Roi, Dame, Valet, 10, 9, 8, 7, 6, 5, 4, 3, 2\}$.  
Nous avons alors $P = C \times V$.
:::

### Famille et sous-famille d'ensembles

Nous généralisons les opérations binaires sur les ensembles à un nombre quelconque d'ensembles.

:::{prf:definition} Famille et sous-famille d'ensembles
Soit $I$ un ensemble, $(E_i)_{i \in I}$ est une **famille** d'ensembles indéxé par $I$ si $\forall i \in I, E_i$ est un ensemble.  
Soient $E$, $I$ des ensembles, $(F_i)_{i \in I}$ une famille d'ensembles.  
$(F_i)_{i \in I}$ est une **sous-famille** de $E$ si $\forall i \in I, F_i \subseteq E$.
:::

Nous posons alors de nouvelles notations pour l'union, l'intersection et le produit cartésien d'une famille d'ensembles.

:::{prf:definition} Réunion et intersection d'une famille d'ensembles
Soit $I$ un ensemble, $(E_i)_{i \in I}$ une famille d'ensembles indéxé par $I$  
La réunion de la famille $(E_i)_{i \in I}$ est l'ensemble $\bigcup_{i \in I} E_i = \{x | \exists i \in I, x \in E_i\}$  
L'intersection de la famille $(E_i)_{i \in I}$ est l'ensemble $\bigcap_{i \in I} E_i = \{x | \forall i \in I, x \in E_i\}$
:::

:::{note}
Le produit cartésien de la famille $(E_i)_{i \in I}$ est noté $\prod_{i \in I}E_i$
:::

## Relations

Comme avec les propositions et les connecteurs logiques, à partir d'ensembles et des opérateurs ensemblistes, nous créons de nouveaux ensembles.  
Avec le produit cartésien aussi, à partir d'un élément d'un ensemble et d'un élément d'un autre ensemble (parfois le même), nous obtenons un couple d'éléments qui sont liés, en `relation`, pour ne former q'un unique élément, appartenant à un nouvel ensemble appelé `graphe` de cette relation.  
Nous allons classer les relations en fonction de leurs propriétés, et enfin étudier un type particulier de relations, les `fonctions`.

:::{prf:definition} Relation binaire
Soient $E$, $F$ des ensembles.  
Soit $G$ un sous-ensemble du produit cartésien de $E$ par $F$, $G \subseteq E \times F$.  
Une **relation binaire** $\mathcal{R}$ de $E$ dans $F$ est un triplet $(E, F, G)$, où $G$ est appelé **graphe** de la relation $\mathcal{R}$  
$\mathcal{R} = \{x, y | x \in E, y \in F, (x, y) \in G\}$, on note alors $x \mathcal{R} y$ ou $\mathcal{R} (x, y)$ et on lit $x$ est en relation, ou en correspondance avec $y$.  
$x$ est l'**antécédent** de $y$ par $\mathcal{R}$ et $y$ est l'**image** de $x$ par $\mathcal{R}$.  
Si $F = E$, $\mathcal{R}$ est une **relation interne** dans $E$, $E$ est muni de la relation $\mathcal{R}$.
:::

:::{prf:definition} Réflexion, symétrie et transitive
Soit $E$ un ensemble muni d'une relation $\mathcal{R}$.  
$\mathcal{R}$ est **réflexive**, si $\forall x \in E$, $x \mathcal{R} x$.  
$\mathcal{R}$ est **symétrique**, si $\forall (x, y) \in E^2$, $x \mathcal{R} y \implies y \mathcal{R} x$.  
$\mathcal{R}$ est **anti-symétrique**, si $\forall (x, y) \in E^2$, $x \mathcal{R} y \: \land \: y \mathcal{R} x \implies x = y$.  
$\mathcal{R}$ est **transitive**, si $\forall (x, y, z) \in E^3$, $x \mathcal{R} y \: \land \: y \mathcal{R} z \implies x \mathcal{R} z$.
:::

:::{prf:definition} Relation d'équivalence
Soit $E$ un ensemble muni d'une relation $\mathcal{R}$.  
$\mathcal{R}$ est une **relation d'équivalence** si $\mathcal{R}$ est réflexive, symétrique et transitive, $x \mathcal{R} y$ se note $x \sim y$.
:::

:::{prf:example}
L'équivalence entre 2 propositions logiques est une relation d'équivalence

- réflexive : pour toute proposition $P$, $P \iff P$.
- symétrique : pour toutes propositions $P$ et $Q$, si $P \iff Q$ alors $Q \iff P$
- transitive : pour toutes propositions $P$, $Q$ et $R$, si $P \iff Q$ et $Q \iff R$, alors $P \iff R$.
:::

:::{prf:definition} Classe d'équivalence
Soient $E$ un ensemble muni d'une relation d'équivalence $\sim$, $x$ un élément de $E$.  
La **classe d'équivalence** de $x$ est l'ensemble des y dans $E$ tel que $x \sim y$, et se note $[x]$  
$[x] = {y \in E | x \sim y}$, $y \in [x] \iff [x] = [y]$
:::

:::{prf:definition} Ensemble quotient
Soit $E$ un ensemble muni d'une relation d'équivalence $\sim$.  
L'**ensemble quotient** $E$ par la relation $\sim$ est le sous-ensemble de $\mathcal{P}(E) des classes d'équivalence, et se note $E/\sim$  
$E/\sim = {[x] \in \mathcal{P}(E) | x \in E}
:::

:::{prf:definition} Relation d'ordre - Ensemble ordonné
Soit $E$ un ensemble muni d'une relation $\mathcal{R}$.  
$\mathcal{R}$ est une **relation d'ordre** si $\mathcal{R}$ est réflexive, anti-symétrique et transitive, $x \mathcal{R} y$ se note $x \leq y$.  
$E$ est alors un **ensemble ordonné**.
:::

:::{prf:example}
L'inclusion est une relation d'ordre

- réflexive : pour tout ensemble $E$, on a $E \subseteq E$.
- antisymétrique : pour tous ensembles $E$ et $F$, si $E \subseteq F$ et $F \subseteq E$, alors $E = F$.
- transitive : pour tous ensembles $E$, $F$ et $G$, si $E \subseteq F$ et $F \subseteq G$, alors $E \subseteq G$.
:::

:::{prf:definition} Ordre total
Soit $E$ un ensemble ordonné muni de $\leq$
$\leq$ est un **ordre total** si $\forall x, y \in E, x \leq y ou y \leq x$.
$E$ est alors un **ensemble totalement ordonné**.
:::

:::{prf:definition} Maximum - Minimum
Soient $E$ un ensemble ordonné, $F$ un sous-ensemble de $E$.  

- Un élément $m$ de $F$ est le **maximum ou plus grand élément** de $F$ si  
$\forall x \in F, x \leq m$.  
- Un élément $m$ de $F$ est le **minimum ou plus petit élément** de $F$ si  
$\forall x \in F, m \leq x$.  
De tels éléments, s'ils existent sont uniques.
:::

:::{prf:definition} Majorant - Minorant
Soient $E$ un ensemble ordonné, $F$ un sous-ensemble de $E$.  

- Un élément $m$ de $E$ est un **majorant** de $F$ si  
$\forall x \in F, x \leq m$.  
- Un élément $m$ de $E$ est un **minorant** de $F$ si  
$\forall x \in F, m \leq x$.  
:::

:::{prf:definition} Ensemble bien ordonné
Soit $E$ un ensemble.
$E$ est bien ordonné si toute partie non vide de $E$ admet un minimum.  
$E$ bien ordonné $\implies $E$ totalement ordonné.
:::

## Fonctions et applications

:::{prf:definition} Fonction
Soient $E$, $F$ et G des ensembles.  
Soient $\mathcal{R}$ une relation de $E$ dans $F$, $G$ le graphe de $\mathcal{R}$.  
La relation $\mathcal{R}$ est une **fonction** de $E$ dans $F$ si, pour tout $x$ appartenant à $E$, il existe 0 ou un seul $y$ appartenant à $F$ tel que $x$ soit en relation en $y$, c'est à dire  
$\forall x \in E, \forall y \in F, \forall z \in F, (x \mathcal{R} y \: \land x \mathcal{R} z) \implies y= z$  
$\mathcal{R}$ se note $f : E \to F$, $x \mathcal{R} y$ se note $f(x) = y$.  
Une notation plus complète d'une fonction $f$ est  
$\begin{align*}
f : E &\to F \\
x &\mapsto y = f(x)
\end{align*}$  
$E$ est le **domaine** de $f$, $F$ est le **codomaine** de $f$.
:::

:::{prf:definition} Domaine de définition, image d'une fonction
Soient $E$ et $F$ des ensembles, $f : E \to F$ une fonction.  
Le **domaine de définition** de $f$ est l'ensemble des éléments de $E$ qui ont une image par $f$, on le note $D_f$.  
$D_f = \{x \in E | \exists y \in F \: \land \: y = f(x)\}$.  
On a $D_f \subseteq E$.  
L'**image** de $f$ est l'ensemble des éléments de $F$ qui ont un antécédent par $f$, on le note $Im(f)$.  
$Im(f) = \{y \in F | y = f(x), x \in E\}$.  
On a $Im(f) \subseteq F$.
:::

:::{prf:definition} Identité
Soit $E$ un ensemble.  
On définit la **fonction identité** de $E$ dans $E$, noté $Id_E$ par  
$\begin{align*}
Id_E : E &\to E \\
x &\mapsto x
\end{align*}$  
$\forall x \in E, Id_E(x) = x$  
Le graphe de $Id_E$ est appelé **diagonale** du produit cartésien $E \times E$.
:::

### Composition de fonctions

:::{prf:definition} Composition de fonctions
Soient $E$, $F$ et $G$ des ensembles, $f : E \to F$, $g : F \to G$ des fonctions.  
La **composée** de $f$ par $g$ est la fonction $g \circ f$  
$\begin{align*}
g \circ f : E &\to G \\
x &\mapsto g \circ f(x) = g(f(x))
\end{align*}$  
$g \circ f$ se lit $g$ rond $f$  
Si $g =f$ alors $f \circ f$ se note $f^2$ et se lit $f$ carré.
:::

### Injection, surjection, bijection

:::{prf:definition} Injection - Surjection - Bijection
Soient $E$ et $F$ des ensembles, $f : E \to F$ une fonction.

- $f$ est **injective** si toute image par $f$ admet un unique antécédent.  
$f$ injective $\iff (\forall x, y \in E, f(x) = f(y) \implies x = y)$.
- $f$ est **surjective** si pour tout $y$ appartenant à $F$, il existe un antécédent $x$ appartenant à $E$ par $f$.  
$f$ surjective $\iff \forall y \in F, \exists x \in E | y = f(x)$.
- $f$ est **bijective** si, et seulement si $f$ est injective et surjective.  
$f$ bijective $\iff \forall y \in F, \exists ! x \in E | y =f(x)$.
:::

:::{prf:definition} Subpotence - Surpotence - Equipotence
Soient $E$ et $F$ des ensembles

- $E$ est **subpotent** à $F$ s'il existe une injection de $E$ dans $F$, et se note $E \preceq F$.  
- $E$ est **surpotent** à $F$ s'il existe une surjection de $E$ dans $F$, et se note $E \succeq F$.  
- $E$ est **équipotent** à $F$ s'il existe une bijection de $E$ dans $F$, et se note $E \approx F$.
:::

:::{prf:theorem} Théorème de Cantor-Berstein
Soient $E$ et $F$ des ensembles.  
Si $E \preceq F$ et $F \preceq E$ alors $E \approx F$
:::

### Fonction réciproque

:::{prf:definition} Bijection réciproque d'une fonction
Soient $E$ et $F$ des ensembles, $f : E \to F$ une fonction bijective, alors il existe une fonction $g : F \to E$ telle que  
$\forall x \in E, g \circ f(x) = x \: \land \: \forall y \in F, f \circ g(y) = y$.  
$g$ est la **fonction réciproque** de $f$, on note $g = f^{-1}$.  
On a $f^{-1} \circ f = Id_E$, $f \circ f^{-1} = Id_F$ et $(f^{-1})^{-1} = f$.  
$f$ est une **involution** si $f^{-1} = f$.
:::

:::{prf:proposition} Réciproque d'une composée
Soient $E$, $F$ et $G$ des ensembles, $f : E \to F$, $g : F \to G$ des fonctions.  
Alors $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
:::

### Application

:::{prf:definition} Application
Soient $E$ et $F$ des ensembles, $f : E \to F$ une fonction.  
$f$ est une **application** si $D_f = E$.  
$f$ est une application $\iff \forall x \in E, \exists ! y \in F | y = f(x)$.
:::
