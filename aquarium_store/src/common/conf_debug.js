export const IS_LOCALHOST = true;

// navigatable: 10 < x < 100 || x > 1000 || x in [no child list]
export const MAIN_DATA = {
  "productCategories": [
    {
      "id": 0,
      "name": "Sản phẩm"
    },
    {
      "id": 1,
      "name": "Cá",
      "hasProducts": true,
      "children": [
        {
          "id": 11,
          "name": "Cá chép",
          "children": [
          ]
        },
        {
          "id": 12,
          "name": "Cá dĩa",
          "children": [
          ]
        },
        {
          "id": 13,
          "name": "Cá rồng",
          "children": [
          ]
        },
        {
          "id": 14,
          "name": "Cá khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 2,
      "name": "Thủy sinh",
      "children": [
        {
          "id": 21,
          "name": "Cây thủy sinh",
          "children": [
          ]
        },
        {
          "id": 22,
          "name": "Đèn thủy sinh",
          "children": [
          ]
        },
        {
          "id": 23,
          "name": "Các thứ khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 3,
      "name": "Động vật khác",
      "children": [
      ]
    },
    {
      "id": 4,
      "name": "Thức ăn",
      "children": [
      ]
    },
    {
      "id": 5,
      "name": "Hồ",
      "children": [
        {
          "id": 51,
          "name": "Hồ cá kiểng",
          "children": [
          ]
        },
        {
          "id": 52,
          "name": "Hồ thủy sinh",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 6,
      "name": "Dụng cụ",
      "children": [
        {
          "id": 61,
          "name": "Đèn cá kiểng",
          "children": [
          ]
        },
        {
          "id": 62,
          "name": "Bơm lọc",
          "children": [
          ]
        },
        {
          "id": 63,
          "name": "Dụng cụ khác",
          "children": [
          ]
        }
      ]
    },
    {
      "id": 7,
      "name": "Linh tinh",
      "children": [
        {
          "id": 71,
          "name": "Trang trí",
          "children": [
          ]
        },
        {
          "id": 72,
          "name": "Thuốc và hóa chất",
          "children": [
          ]
        }
      ]
    },

    {
      "id": 0,
      "name": "Bài viết"
    },
    {
      "id": 100,
      "name": "Hướng dẫn setup",
      "children": [
      ]
    },
    {
      "id": 200,
      "name": "Mẹo",
      "children": [
        {
          "id": 2001,
          "name": "Mẹo chăm sóc",
          "children": [
          ]
        },
        {
          "id": 2002,
          "name": "Mẹo phong thủy",
          "children": [
          ]
        }
      ]
    }
  ],

  "products": {
    "11": [1, 2],
    "13": [3, 4],
    "14": [7, 8, 9]
  },

  "product": {
    "1": {
      "name": "Cá chép thường",
      "priceMin": 0,
      "priceMax": 0,
      "imgUrl": "https://1.bp.blogspot.com/-RvLQKePt1gs/X6N4ukn1VpI/AAAAAAAAABA/TPamOOjKZtgJjhmnjapN5HfArCoTeMLkwCNcBGAsYHQ/s16000/CaKieng.jpg",
      "desc": "Cá chép \"thường\"",
      "briefImgUrl": "https://1.bp.blogspot.com/-YLQ9Ye1iNlM/X6OBp_iwMRI/AAAAAAAAABk/GukXkgUSFZk8ArZeVp-ZjURSdduPjGvDACNcBGAsYHQ/s16000/CaKieng.jpg"
    },
    "2": {
      "name": "Cá chép koi",
      "priceMin": 20,
      "priceMax": 50,
      "imgUrl": "https://1.bp.blogspot.com/-RvLQKePt1gs/X6N4ukn1VpI/AAAAAAAAABA/TPamOOjKZtgJjhmnjapN5HfArCoTeMLkwCNcBGAsYHQ/s16000/CaKieng.jpg",
      "desc": "Cá \"chép\" koi",
      "briefImgUrl": "https://1.bp.blogspot.com/-YLQ9Ye1iNlM/X6OBp_iwMRI/AAAAAAAAABk/GukXkgUSFZk8ArZeVp-ZjURSdduPjGvDACNcBGAsYHQ/s16000/CaKieng.jpg"
    },
    "3": {
      "name": "Ngân long",
      "priceMin": 700,
      "priceMax": 1200,
      "imgUrl": "https://1.bp.blogspot.com/-Ave4gT3_KoI/X6UOWP0o2JI/AAAAAAAAACQ/6jY02uG8POEpr354--EkSaoKh7d-lzHTgCNcBGAsYHQ/s16000/nganlong.jpg",
      "desc": "Ngân long",
      "briefImgUrl": "https://1.bp.blogspot.com/-47ARAjPsaTY/X6USxyVJXSI/AAAAAAAAACs/S18sDAgueWcftz73P5qkRdsUCPFxrlpHgCNcBGAsYHQ/s16000/nganlong.jpg"
    },
    "4": {
      "name": "Kim long",
      "priceMin": 1000,
      "priceMax": 2000,
      "imgUrl": "https://1.bp.blogspot.com/-Qq4GCAcjDww/X6UON5Zu4_I/AAAAAAAAACI/Rf0q__YxLhkUlmMKCEohoOxP-PSwZGreQCNcBGAsYHQ/s16000/kimlong.jpg",
      "desc": "Kim long",
      "briefImgUrl": "https://1.bp.blogspot.com/-lxxakkgQDBM/X6USosKhKcI/AAAAAAAAACo/GgBtsmJJetki8Yx-JhPCv9QaWpKSekR6wCNcBGAsYHQ/s16000/kimlong.jpg"
    },
    "7": {
      "name": "Cá ông tiên",
      "priceMin": 10,
      "priceMax": 30,
      "imgUrl": "https://1.bp.blogspot.com/-EEHwqticPPE/X6N_fo25iXI/AAAAAAAAABU/Qxqb4Pm7_fcYZ2mZJTwkbFbekxw7G5WnwCNcBGAsYHQ/s16000/CaOngTien.jpg",
      "desc": "Cá ông tiên đẹp ăn trùng chỉ,  điệu kiện nước đòi hỏi pH, nhiệt độ thích hợp. Đòi hỏi chăm sóc kỹ lưỡng.",
      "briefImgUrl": "https://1.bp.blogspot.com/-wxwlP3G9-Hk/X6OCB1MIvWI/AAAAAAAAAB0/XmZPHAoXgccBJNIThKNCkqAUtOPHt2JgQCNcBGAsYHQ/s16000/CaOngTien.jpg"
    },
    "8": {
      "name": "Cá La Hán",
      "priceMin": 20,
      "priceMax": 40,
      "imgUrl": "https://1.bp.blogspot.com/-LcHPXV6u9A8/X6UOdgzkc1I/AAAAAAAAACY/mVXG9rHy4ecbFEvop2TyV0Npx2vxr9NtwCNcBGAsYHQ/s16000/lahan.jpg",
      "desc": "Cá La Hán ăn trùng chỉ dễ nuôi, đòi hỏi thay nước thường xuyên để tránh bệnh nấm mốc gây ra cho cá.",
      "briefImgUrl": "https://1.bp.blogspot.com/-FIiAhqIt_vI/X6UTfZy_gUI/AAAAAAAAAC4/eoUYBW8EU-EsM4itPi2UcP1_PCyTwywWACNcBGAsYHQ/s16000/lahan.jpg"
    },
    "9": {
      "name": "Cá ba đuôi",
      "priceMin": 0,
      "priceMax": 0,
      "imgUrl": "https://1.bp.blogspot.com/-ubb-9u66o88/X6UODLx4BKI/AAAAAAAAACE/P2s0rRoTqhsOoXNOjnMMdDFheUtAeuVJACNcBGAsYHQ/s16000/baduoi.jpg",
      "desc": "Cá ba đuôi ăn cám viên hoặc trùng chỉ, chăm sóc dễ, cẩn thận không cho cá ăn quá nhiều kẻo chết cá vì cá rất ham ăn.",
      "briefImgUrl": "https://1.bp.blogspot.com/-bhT0iVNgzFg/X6UTZHYi6-I/AAAAAAAAAC0/wV3yPd4f4w8mOn1AxntWNEvtWbgexmM7ACNcBGAsYHQ/s16000/baduoi.jpg"
    }
  }
};