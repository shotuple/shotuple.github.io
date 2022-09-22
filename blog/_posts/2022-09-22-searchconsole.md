---
layout: post
title: Jekyll 구글 검색 노출

description: >
  Search Console을 이용한 구글 검색 노출

tags:
 - [Blog, jekyll, Github, Git]

toc: true
toc_sticky: true

date: 2022-09-14
last_modified_at: 2022-09-14

sitemap: false

---
---

## 1. Search Console 시작하기
[Search Console](https://developers.google.com/search#?modal_active=none) 접속

### URL 접두어 선택 후, https://username.github.io/ 을 입력하고 계속을 클릭합니다.

### 하단 다른 확인 방법의 HTML 태그 선택 후, 메타태그를 복사합니다.

### 메타 태그를 txt파일에 붙여넣으면 나오는 내용입니다.
> meta name="google-site-verification" content="**1gDBG.........................................._stqA**"

### _config_yml 의 google_site_verification 항목을 찾아 content 부분을 붙여넣어줍니다.
> google_site_verification: **1gDBG.........................................._stqA**

### git push 후 deploy가 끝날 때까지 기다립니다.

### 메타태그를 복사했던 브라우저 창으로 돌아와서 확인을 클릭합니다.
<br/>

## 2. Sitemap.xml 만들고 push합니다.
### root 경로에 sitemap.xml 파일을 만들어줍니다.
```
---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  {% for post in site.posts %}
    <url>
      <loc>{{ site.url }}{{ post.url }}</loc>
      {% if post.lastmod == null %}
        <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
      {% else %}
        <lastmod>{{ post.lastmod | date_to_xmlschema }}</lastmod>
      {% endif %}

      {% if post.sitemap.changefreq == null %}
        <changefreq>weekly</changefreq>
      {% else %}
        <changefreq>{{ post.sitemap.changefreq }}</changefreq>
      {% endif %}

      {% if post.sitemap.priority == null %}
          <priority>0.5</priority>
      {% else %}
        <priority>{{ post.sitemap.priority }}</priority>
      {% endif %}

    </url>
  {% endfor %}
</urlset>
```
<br/>

## 3. sitemap.xml 등록하기
### Google Search Console > Sitemaps > 새 사이트맵 추가 부분에 sitemap.xml을 입력하고 제출을 클릭합니다.

![image](https://user-images.githubusercontent.com/105637541/191681920-76146607-8600-4acf-82c4-91d4e9c551ba.png)
<br/>

## 4. 결과 확인
제출에 성공했어도 바로 구글 검색에 노출되는 것은 아닙니다. 짧게는 하루에서 길게는 일주일 정도 걸릴 수 있습니다.
