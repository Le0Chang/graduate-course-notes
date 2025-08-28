## Course Grading & Assessment
Course grades will be based on four components: Homework, Midterm, Final, Participation.

These are described individually below. I would like to maximize the course score that I give each 
of you. To optimize each student's course score, I will solve the following optimization problem:

Denote the student’s performance in each of these four components as

$$
\begin{cases}
{𝐶_𝐻} = 𝐻𝑜𝑚𝑒𝑤𝑜𝑟𝑘 𝑠𝑐𝑜𝑟𝑒&(𝑜𝑢𝑡 𝑜𝑓 100),\\
{𝐶_M} = 𝑀𝑖𝑑𝑡𝑒𝑟𝑚 𝐸𝑥𝑎𝑚 𝑠𝑐𝑜𝑟𝑒&(𝑜𝑢𝑡 𝑜𝑓 100),\\
{𝐶_F} = 𝐹𝑖𝑛𝑎𝑙 𝐸𝑥𝑎𝑚 𝑠𝑐𝑜𝑟𝑒&(𝑜𝑢𝑡 𝑜𝑓 100),\\
{𝐶_P} = 𝑃𝑎𝑟𝑡𝑖𝑐𝑖𝑝𝑎𝑡𝑖𝑜𝑛 𝑠𝑐𝑜𝑟𝑒&(𝑜𝑢𝑡 𝑜𝑓 100).
\end{cases}
$$

Then a rubric for grading this student is given by selecting weights for these four components as

$$
\begin{cases}
𝐻 = 𝐻𝑜𝑚𝑒𝑤𝑜𝑟𝑘 𝑤𝑒𝑖𝑔ℎ𝑡,\\
𝑀 = 𝑀𝑖𝑑𝑡𝑒𝑟𝑚 𝐸𝑥𝑎𝑚 𝑤𝑒𝑖𝑔ℎ𝑡,\\
𝐹 = 𝐹𝑖𝑛𝑎𝑙 𝐸𝑥𝑎𝑚 𝑤𝑒𝑖𝑔ℎ𝑡,\\
𝑃 = 100 − 𝐻 − 𝑀 − 𝐹 ,
\end{cases}
$$

(Notice the participation weight is determined by the other three since they must sum to 100).

Each student’s score is given by maximizing over the set of all reasonable rubrics by solving

$$
\begin{cases}
Max (𝐶_𝐻𝐻 + 𝐶_𝑀𝑀 + 𝐶_𝐹𝐹 + 𝐶_𝑃(100 − 𝐻 − 𝑀 − 𝐹))/100\\
𝑜𝑣𝑒𝑟 𝑎𝑙𝑙 𝑡𝑟𝑖𝑝𝑙𝑒𝑠 (𝐻, 𝑀, 𝐹) ∈ ℝ^3\\
 𝐻 + 𝑀 + 𝐹 ≤ 100\\
 𝐻 ≥ 15\\
 𝑀 ≥ 15\\
 𝐹 ≥ 𝑀\\
 𝑀 + 𝐹 ≥ 50\\
 𝑀 + 𝐹 ≤ 80\\
 𝐻 + 𝑀 + 𝐹 ≥ 90
 \end{cases}
$$
