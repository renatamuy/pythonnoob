seg_str = input("Quantos segundos deseja converter? ")
total_segs = int(seg_str)

segsdia = (60 * 1 * 60 * 24)

dias = total_segs //segsdia
segs_restantes_dia = total_segs % segsdia
horas = segs_restantes_dia // 3600
segs_restantes = segs_restantes_dia % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
