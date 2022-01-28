
def respawn():
    from autospawner.spawner import Spawner
    spawner = Spawner()
    if not spawner.shouldSpawn():
        print('Not appropriate to spawn at this time')
        return -1
    shard = spawner.getShard()
    room = spawner.getRoom(shard)
    position = spawner.getPosition(room, shard)
    print("%s %s %s,%s" % (shard, room, position['x'], position['y']))
    if spawner.respawn(shard, room, position):
        print('Respawn complete')
    else:
        print('Respawn Failed')
        return -1

if __name__ == '__main__':
    respawn()
