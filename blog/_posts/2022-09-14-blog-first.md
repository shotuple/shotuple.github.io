---
layout: post
title: Github 블로그 생성 + Jekyll

description: >
  Github page로 블로그를 만듭니다.

tags:
 - [Blog, jekyll, Github, Git]

toc: true
toc_sticky: true

date: 2022-09-14
last_modified_at: 2022-09-14

sitemap: false

---
---

## 1. Repository 생성
~~~
Repository name: username.github.io로 생성합니다.
※ Public으로 설정해야 사용자가 블로그에 접근할 수 있습니다!
~~~

## 2. Repository clone
### 아래 초록색 Code 버튼을 클릭하면 나오는 https 주소를 복사해줍니다!
![image](https://user-images.githubusercontent.com/105637541/190078338-5b2d3e99-33b5-4d34-b71f-0942c19941b6.png)

### git bash에서 
~~~git
git clone 주소붙여넣기(shift+insert)
~~~

간단한 index.html을 만들고 github의 원격 저장소로 올려서 username.github.io로 접속하는 과정이 있으나, 생략하고 우선 Jekyll theme를 적용한 후 진행합니다! 

## 3. 블로그 꾸미기
  

### Jekyll theme 다운로드   
추천 테마 : <http://themes.jekyllrc.org/hydejack/>  

### 혹은 아래에서 끌리는 theme 선택  
<http://jekyllthemes.org/>  
<https://jekyllthemes.io/free>  
<https://jamstackthemes.dev/ssg/jekyll/>  
<https://jekyll-themes.com/free/>

### 다운로드한 theme를 2에서 clone한 username.github.io 폴더에 넣어줍니다. (덮어쓰기)

## 3.2 Ruby, jekyll 설치
[Ruby 다운로드 링크](https://rubyinstaller.org/downloads/)  

![image](https://user-images.githubusercontent.com/105637541/190083336-38bccca4-9db0-427c-bcf5-c083620c5f90.png)  

=> 표시와 함께 볼드된 링크를 다운로드합니다. Next만 누르면 설치 완료! 이후 MSYS2 설치도스에선 1을 입력하고 엔터합니다. 설치하면 Ruby 명령어를 cmd 창에서도 실행가능합니다!

## 4. 번들 설치, jekyll을 로컬 서버에 띄우기
![image](https://user-images.githubusercontent.com/105637541/190084550-e3ff3b6e-855a-414e-ac1b-997023ab136a.png)
### Ruby 설치가 완료되면 상기 Prompt 혹은 cmd 창을 열어줍니다!
~~~Ruby
cd "C:\Users\user\Desktop\Git\username.github.io"

chcp 65001 (명령어에서 발생하는 오류를 방지합니다.)

gem install bundler
gem install jekyll

bundle install
bundle exec jekyll serve
~~~
![image](https://user-images.githubusercontent.com/105637541/190086882-dcd12803-703f-4b06-93a5-9b3180c388f0.png)  
### 결과가 이렇게 나오면 성공입니다!
<http://127.0.0.1:4000/>   로 접속합니다.

## 5. Push
### 로컬에서 작동하는 것을 확인했습니다. 
#### 이제 Github 원격 저장소에 저장해서 username.github.io를 통해 접속합니다.  
  

Git Bash 상에서
~~~git
git add .
git commit -m "Blog"
git push
~~~

### username.github.io로 접속합니다!






