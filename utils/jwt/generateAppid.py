import uuid
import hashlib

# generate appid
def generate_app_id(username, email, password):
  app_id = uuid.uuid3(uuid.NAMESPACE_OID, '{}-{}-{}'.format(username, email, password))
  app_id = app_id.__repr__()[6:-2]
  return app_id