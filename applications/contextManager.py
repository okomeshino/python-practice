# encoding:utf-8
class ContextManagerTest:

    # 開始時の処理
    def __enter__(self):
        print('__enter__')
        # asで渡されたオブジェクトを処理して返す（無くても良い）
        return 'as obj'

    # 終了時の処理
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with ContextManagerTest() as as_obj:
    print(as_obj)
