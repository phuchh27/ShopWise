from .models import Store

def check_owmer(store_id , user):
    try: 
        store = Store.objects.get(id=store_id)
        return store.owner == user
    except Store.DoesNotExist:
        return False

class StoreService:
    @staticmethod
    def get_store_ids_by_owner(owner_id):
        store_ids = Store.objects.filter(owner_id=owner_id, is_active=True).values_list('id', flat=True)
        return list(store_ids)   
    
    @staticmethod
    def get_owner_id_by_store_id(store_id):
        try:
            store = Store.objects.get(id=store_id)
            owner_id = store.owner_id
            return owner_id
        except Store.DoesNotExist:
            return None