<- env ->
что нужно установить из енв??

pip install python-decouple
pip install flask
pip install psycopg2
 

 <- settings ->

dbname   = 'forum'
user     = 'postgres'
password = 'admin'
host     = 'localhost'


 >>> ! ЕНД-П0ИНТЫ ! <<<

'/' - страница регистрации (после регистрации идем в авторизацию)
'/authorization' - страница авторизации 
'/posts' - главная страница с постами
'/post/{{(айди поста)}}' - собственная страница поста там и комменты


 <- errors - > 

1 - process didnt bla bvla
2 - passwords x x
3 - empty polya
4 - юзер неправильно ввел поле is_author yes\no

времени на нормальный дизайн не хватило,
но в целом все подзадачи выполнены и все работает
можете тестить

СПАСИБО ЗА ВНИМАНИЕ!
