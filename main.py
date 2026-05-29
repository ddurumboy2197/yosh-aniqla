def tugilgan_yil_orqali_yoshni_analiz(qidirilayotgan_yosh, tugilgan_yil):
    yosh = 2024 - tugilgan_yil
    if yosh == qidirilayotgan_yosh:
        return True
    elif yosh > qidirilayotgan_yosh:
        return False
    else:
        return "Yoshni aniqlash mumkin emas"

print(tugilgan_yil_orqali_yoshni_analiz(25, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(30, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(25, 2024))
```

```python
def tugilgan_yil_orqali_yoshni_analiz(qidirilayotgan_yosh, tugilgan_yil):
    yosh = 2024 - tugilgan_yil
    return yosh == qidirilayotgan_yosh

print(tugilgan_yil_orqali_yoshni_analiz(25, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(30, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(25, 2024))
```

```python
def tugilgan_yil_orqali_yoshni_analiz(qidirilayotgan_yosh, tugilgan_yil):
    yosh = 2024 - tugilgan_yil
    return yosh >= qidirilayotgan_yosh

print(tugilgan_yil_orqali_yoshni_analiz(25, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(30, 1999))
print(tugilgan_yil_orqali_yoshni_analiz(25, 2024))
