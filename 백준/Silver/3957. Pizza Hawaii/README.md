# [Silver I] Pizza Hawaii - 3957 

[문제 링크](https://www.acmicpc.net/problem/3957) 

### 성능 요약

메모리: 31120 KB, 시간: 84 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현

### 제출 일자

2024년 11월 15일 11:26:14

### 문제 설명

<p>You are travelling in a foreign country. Although you are also open to eat some regional food, you just cannot resist after you have found an Italian restaurant which offers pizza. Unfortunately the menu is written in the foreign language, so the list of ingredients of the pizzas are incomprehensible to you. What will you do?</p>

<p>One thing that you notice is that each pizza has an Italian name, which sounds quite familiar to you. You even remember for each named pizza what the ingredients of this pizza usually are. You want to use that information to figure out what the possible meaning of each word on the list of ingredients is.</p>

### 입력 

 <p>The first line of the input gives the number of test cases t (0 < t ≤ 20). The first line of each input gives the number n of pizzas on the menu (1 ≤ n ≤ 60). The following 3·n lines describe the pizzas on the menu. Each pizza description starts with one line containing the name of the pizza. The name of the pizza consists of between 3 and 20 uppercase and lowercase letters. The next line starts with an integer m<sub>i</sub>, giving the number of ingredients of the pizza on the menu (1 ≤ m<sub>i</sub> ≤ 20). The rest of the line contains the m<sub>i</sub> ingredients separated by spaces. Each ingredient is a word consisting of between 2 and 20 lowercase letters. The third line of each pizza description gives the ingredients in your native language in the same format. Note that the number of ingredients may differ, because each restaurant may use slightly different ingredients for pizzas with the same name, so the ingredients you remember for a pizza with that name may not match the actual ingredients.</p>

### 출력 

 <p>For each test case print all pairs of words (w<sub>1</sub>, w<sub>2</sub>) where w1 is an ingredient in the foreign language that could be the same ingredient as w<sub>2</sub> because w<sub>1</sub> and w<sub>2</sub> appear on the same set of pizzas. Sort the pairs in increasing lexicographical order by w<sub>1</sub>, and in case of a tie in increasing lexicographical order by w<sub>2</sub>. Print a blank line between different test cases.</p>

