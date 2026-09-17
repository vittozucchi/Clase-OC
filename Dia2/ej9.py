frutas={
    "manzanas":100,
    "banana":50,
    "naranja":80,
}

user1=str(input("que fruta quiere?: "))
user2=float(input("cuantos kg quiere?: "))

calc=frutas.get(user1, "no encontrada")

calcu=calc*user2
print("la fruta cuesta ",calcu)