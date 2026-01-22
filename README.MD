# DSS PO Dashboard

Decision Support System (DSS) untuk rekomendasi Purchase Order berbasis
**Days of Inventory on Hand (DOI)** dengan mempertimbangkan **lead time**.

## Tujuan
Membantu pengambilan keputusan PO agar:
- mengurangi risiko stockout
- menghindari overstock
- tetap memberi ruang judgement manusia

## Konsep DSS
Sistem ini **tidak mengotomasi keputusan sepenuhnya**.
Beberapa parameter (mis. rata-rata penjualan) bersifat **judgement bisnis**
agar keputusan tetap kontekstual.

## Rule DSS (V1)
- DOI < threshold → **LAYAK PO**
- DOI di rentang threshold → **MONITOR**
- DOI > threshold → **TUNDA PO**

Threshold disesuaikan secara dinamis dengan **lead time (hari)**.

## Tech Stack
- Backend: Django, Django Rest Framework
- Frontend: React (Vite)
- Database: SQLite (development)

## Struktur Project
