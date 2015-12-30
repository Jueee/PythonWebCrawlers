import re
s ='''


<div class="zm-item" id="mi-1392377669">
<h2><a class="question_link" href="/question/22656916/answer/22478174">我发现微博上的程序员大多的都是单身男？</a></h2>
<div tabindex="-1" class="zm-item-answer zm-item-answer-owner"
data-aid="4194384"
data-atoken="22478174"
data-collapsed="0"
data-created="1392377669"
data-deleted="0"
data-isowner="1"
data-helpful="1"
data-copyable="1"
>
<a class="zg-anchor-hidden" name="answer-4194384"></a>

<div class="zm-item-vote">
<a class="zm-item-vote-count js-expand js-vote-count" href="javascript:;" data-votecount="2">2</a>
</div>


<div class="answer-head">

<div class="zm-item-answer-author-info">

<a class="zm-item-link-avatar avatar-link" href="/people/jueee" data-tip="p$t$jueee">
<img src="https://pic4.zhimg.com/a31c668e7_s.jpg" class="zm-list-avatar avatar">
</a>

<a class="author-link" data-tip="p$t$jueee" href="/people/jueee">尉勇强</a><span title="God help someone who wants more." class="bio">，God help someone who wants more.</span>
</div>

<div class="zm-item-vote-info " data-votecount="2">

<span class="voters">
<span class="user-block"><a data-tip="p$t$ying-ying-candice" href="https://www.zhihu.com/people/ying-ying-candice" class="zg-link" title="莹莹candice">莹莹candice</a>、</span><span class="user-block"><a data-tip="p$t$lanisle" href="https://www.zhihu.com/people/lanisle" class="zg-link" title="lanisle">lanisle</a></span>
</span>


<span>赞同</span>


</div>
</div>
<div class="zm-item-rich-text js-collapse-body" data-resourceid="1243489" data-action="/answer/content" data-author-name="尉勇强" data-entry-url="/question/22656916/answer/22478174">

<textarea class="content hidden">
一、实在不会打扮，比较挫；&lt;br&gt;二、一般也比较不会说话，不会讨女孩子开心；&lt;br&gt;三、认识女孩子机会少；&lt;br&gt;四、加班累死累活的多；&lt;br&gt;&lt;br&gt;等


<span class="answer-date-link-wrap">
<a class="answer-date-link meta-item" target="_blank" href="/question/22656916/answer/22478174">发布于 2014-02-14</a>
</span>

</textarea>


<div class="zh-summary summary clearfix">

一、实在不会打扮，比较挫；二、一般也比较不会说话，不会讨女孩子开心；三、认识女孩子机会少；四、加班累死累活的多；等

</div>


</div>
<div class="zm-item-meta zm-item-comment-el answer-actions clearfix">
<div class="zm-meta-panel">

<a data-follow="q:link" class="follow-link zg-follow meta-item" href="javascript:;" id="sfb-1243489"><i class="z-icon-follow"></i>关注问题</a>

<a href="#" name="addcomment" class=" meta-item toggle-comment">
<i class="z-icon-comment"></i>添加评论</a>


<a href="#" class="meta-item zu-autohide" name="share">
<i class="z-icon-share"></i>分享</a>
<a href="#" class="meta-item zu-autohide" name="favo">
<i class="z-icon-collect"></i>收藏</a>


<a href="#" class="meta-item zu-autohide" name="comment_opt" data-copyable="true"><i class="zg-icon zg-icon-settings"></i>设置</a>





<span class="zg-bull">&bull;</span>

<a href="/terms#sec-licence-1" target="_blank" class="meta-item copyright"> 作者保留权利 </a>


<button class="meta-item item-collapse js-collapse">
<i class="z-icon-fold"></i>收起
</button>
</div>

</div>
</div>
</div>
'''
matchs = re.finditer(r'<div class="zm-item"([\s\S]*)<i class="z-icon-fold">',s)
for match in matchs:
    print(match.group(1))