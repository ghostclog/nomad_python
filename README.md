# nomad_python

## 노마드 코더 파이썬 10주 스터디 첫번째 졸업작품(파이썬)입니다.
- 작업기간(Working period): 2024.08.20~2024.08.21
- 프로젝트 인원은 1명으로 개인으로 진행하였습니다.
- 디자인이 이틀가량 소모되었고, 구현이 하루가량 소모되었습니다.(The design consumed about two days, and the implementation consumed about a day.)

## 구현 목표 및 핵심 기능
- 특정 키워드 입력시 사용자가 선택한 옵션에 따라 구인 공고를 찾아서 사용자에게 제공
- 구인 공고를 csv형태로 다운로드 기능

## 사용 기술 및 라이브러리
- 핵심 기술: 웹스크랩핑, 웹서버 구축
- 사용 라이브러리: 플라스크, beautifulSoap4, requests
- 스크랩핑에 사용된 사이트(Site used for Scrapping): berlinstartupjobs / web3.career

## 사이트 설명
- 초기페이지(init page)
![초기_페이지](https://github.com/user-attachments/assets/854d4848-f2dc-4bea-bf25-d8d1d6a165d5)

기본 접속시 볼 수 있는 사이트입니다. 상단의 라디오 버튼을 통해 특정 사이트의 결과만 볼 것인지. 아니면, 모든 사이트의 결과를 종합해서 볼 것인지 선택 할 수 있습니다. <br>
This is the default site for viewing. You can choose whether you want to view only the results of a specific site through the radio button at the top. Or, you can choose to view the results of all sites together.

<br>

- 키워드 검색 후(after search keyword)
![키워드_검색_후](https://github.com/user-attachments/assets/ace661cd-208e-441c-8a2e-01d026a4a93b)

키워드 검색 이후, 선택한 사이트에서 스크랩핑한 데이터들을 화면에 뿌려줍니다. <br>
After searching for keywords, data clipped by the selected site is scattered on the screen.

<br>

- 키워드 검색시, 링크(after search keyword, link)

  <br>

![링크](https://github.com/user-attachments/assets/3cbb2670-3d2e-4a47-b602-6e1c0386b0b0)

사이트는 전반적으로 get 방식을 사용하며, keyword와 site라는 파라미터가 사용됩니다. <br>
The site generally uses the get method, and the parameters keyword and site are used.

<br>

- html 문서 수정으로 인한 xss 공격시.(For xss attack due to html document modification)

![사이트 관련 처리 부분](https://github.com/user-attachments/assets/b0bf60de-b315-4568-97cb-dac32f65d68d)

site의 파라미터에 한해서 사이트에서 처리 가능한 값만 받을 수 있게 설정해놨으며, 그 외의 데이터가 들어올 경우 기본 주소(/)로 리다이랙트되도록 구현해놨습니다. <br>
Only the parameters of the site are set to receive values that can be processed by the site, and if other data are received, it is implemented to be redirected to the default address (/).

### 작업한 replit link: https://replit.com/@ghoostdog/PythonGraduate#main.py
