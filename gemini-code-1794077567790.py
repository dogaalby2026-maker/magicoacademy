import zipfile
import os

# Create project structure in memory/disk and zip it
os.makedirs('mageco_academy', exist_ok=True)

html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أكاديمية الماجيكو لكرة القدم</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>body { font-family: 'Cairo', sans-serif; }</style>
</head>
<body class="bg-blue-950 text-right min-h-screen flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full border-t-8 border-blue-600">
        <div class="text-center mb-6">
            <img src="https://scontent.fcai19-12.fna.fbcdn.net/v/t39.30808-6/355342711_1457038988389922_15423102352844252_n.jpg?stp=dst-jpg_tt6&cstp=mx720x720&ctp=s720x720&_nc_cat=100&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=KSHzCUPUtNMQ7kNvwFiQTrI&_nc_oc=AdpvWLGKV7N9Axx9afLJtyRJsBQtATp2rWJAsxXjg8si9KDXFcZej0ujSs8cimN4dxM&_nc_zt=23&_nc_ht=scontent.fcai19-12.fna&_nc_gid=hQC-sPUNbqUmXE4NC-ft7g&_nc_ss=7b2a8&oh=00_AQQYzPabByQL2a6pxDL5kfY8pGNVBHpu5Z0jjQtzV0FANA&oe=6AE9E715" alt="لوجو الأكاديمية" class="w-28 h-28 mx-auto rounded-full object-cover shadow-md border-4 border-blue-100 mb-3">
            <h1 class="text-2xl font-black text-blue-900">أكاديمية الماجيكو لكرة القدم</h1>
            <p class="text-sm text-gray-500 mt-1">النهاردة حلم ........ بكره بطل</p>
        </div>

        <div class="space-y-4">
            <div class="bg-blue-50 p-4 rounded-xl border border-blue-200">
                <h2 class="font-bold text-blue-900 mb-2">دخول الإدارة والجهاز الفني</h2>
                <input type="text" id="adminName" placeholder="اسم الكابتن / المدير" class="w-full p-2.5 mb-2 border rounded-lg text-sm bg-white">
                <input type="password" id="adminPass" placeholder="كلمة المرور (adminM)" class="w-full p-2.5 mb-3 border rounded-lg text-sm bg-white">
                <button onclick="loginAdmin()" class="w-full bg-blue-700 hover:bg-blue-800 text-white font-bold py-2.5 rounded-lg transition">دخول الإدارة</button>
            </div>

            <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-200">
                <h2 class="font-bold text-indigo-900 mb-2">دخول ولي الأمر</h2>
                <input type="text" placeholder="اسم اللاعب" class="w-full p-2.5 mb-2 border rounded-lg text-sm bg-white">
                <input type="password" placeholder="رمز ولي الأمر (4 أرقام)" class="w-full p-2.5 mb-3 border rounded-lg text-sm bg-white" maxlength="4">
                <button onclick="alert('أهلاً بك يا ولي الأمر، سيتم تفعيل اللوحة المخصصة فور ربط البيانات.')" class="w-full bg-indigo-700 hover:bg-indigo-800 text-white font-bold py-2.5 rounded-lg transition">متابعة ابني</button>
            </div>
        </div>
    </div>

    <script>
        function loginAdmin() {
            const name = document.getElementById('adminName').value;
            const pass = document.getElementById('adminPass').value;
            if