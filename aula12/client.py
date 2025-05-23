import grpc
import cube_pb2
import cube_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cube_pb2_grpc.CubeServiceStub(channel)
        
        response = stub.GetCube(cube_pb2.NumberRequest(number=3))
        print(f"Cubo de 3 é: {response.result}")

if __name__ == "__main__":
    run()
