# [Gold IV] H-index - 23950 

[문제 링크](https://www.acmicpc.net/problem/23950) 

### 성능 요약

메모리: 52900 KB, 시간: 6096 ms

### 분류

애드 혹, 자료 구조, 우선순위 큐

### 제출 일자

2024년 8월 24일 10:57:53

### 문제 설명

<p>It is important for researchers to write many high quality academic papers. Jorge has recently discovered a way to measure how impactful a researcher's papers are: the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank">H-index</a>.</p>

<p>The <i>H-index score</i> of a researcher is the largest integer h such that the researcher has h papers with at least h citations each.</p>

<p>Jorge has written <b>N</b> papers in his lifetime. The i-th paper has <b>A<sub>i</sub></b> citations. The number of citations that each paper has will never change after it is written. Please help Jorge determine his H-index score after each paper he wrote.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing <b>N</b>, the number of papers Jorge wrote.</p>

<p>The second line contains <b>N</b> integers. The i-th integer is <b>A<sub>i</sub></b>, the number of citations the i-th paper has.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is a space-separated list of integers. The i-th integer is the H-index score after Jorge wrote his i-th paper.</p>

