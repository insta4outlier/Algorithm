# advice of problem solving

### 잘못된 알고리즘의 사용
슬프게도, 초심자일수록 자주, 알고리즘 자체가 잘못된 경우가 많습니다. <br/>
알고리즘을 전산학적으로 다루는 경우 크게 두 가지에 대해 배웁니다. 바로 알고리즘의 정당성(correctness) 증명과 시간/공간복잡도(efficiency) 분석이지요. 알고리즘이 잘못되었거나 답이 나오는 데 너무 오랜 시간이 걸리는 경우 오답이 됩니다.
<br/>
<br/>
위에서 설명했듯 크게 두 가지로 나뉩니다.

### 틀린 알고리즘
알고리즘이 왜 맞는지 논리적으로 설명할 자신이 있는지 잘 생각해 보세요. 그 자체로 좋은 공부가 됩니다. <br/>
특히 특별한 경우, 최대값이나 최소값, 또는 경계 조건 같은 것들을 깊이 검토해 보세요. <br/>
알고리즘이 맞는지 틀린지 자신이 없다면, 데이터를 좀 더 넣어보면 도움이 됩니다. 이 때, 다음 두 가지를 준비해서 비교해보는 것이 좋습니다. 작은 데이터에서 맞다면, 많은 경우 큰 데이터에서도 맞게 마련이지요. <br/>
- 랜덤한 데이터를 만드는 프로그램
- 느려서 작은 데이터만 풀 수 있지만, 확실히 틀리지 않을 알고리즘

### 절대 시간 안에 답이 나오지 않는 알고리즘
때로는 우주가 끝날 때까지 답이 나오지 않을 수도 있습니다. 채점자 입장에서는 알 수 없기 때문에, 일정 시간이 지나면 오답처리하고 종료하는 수밖에는 없습니다. <br/>
얼마만큼의 시간이 걸릴지 어림잡아 보세요. 예를 들어, C/C++의 경우 조건문이나 덧셈 같은 연산이 1억번 정도 되면 1초 정도 걸린다고 어림할 수 있습니다. (다른 언어는 훨씬 복잡하지요) <br/>
아슬하게 시간에 걸리는 경우는 보통 없습니다. 구현의 방법에 따라서 같은 알고리즘도 두세 배씩은 느릴 수 있습니다. 아예 방법이 잘못된 경우, 시간 제한이 1초인 문제에 대해 10초, 1시간, 1년, 혹은 그 이상이 걸리게 됩니다.

<br/>

출처: [ALGOSPOT 자주하는 실수모음](https://www.algospot.com/wiki/read/%EC%9E%90%EC%A3%BC_%ED%95%98%EB%8A%94_%EC%8B%A4%EC%88%98_%EB%AA%A8%EC%9D%8C)