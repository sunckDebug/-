# - 玩家分数数排行榜

## -接口一
#### - 客户端上客户端号和分数  当前接口使用http get传参   http://127.0.0.1:8000/app/submit?name=客户六&score=20
#### - 其中name参数必填 score可填可不填


## -接口二
#### - 客户端查询分数排行榜  当前接口使用http get传参   http://127.0.0.1:8000/app/ranking?start=1&end=3
#### - start和end 必填两个或不填 不填即为全查询