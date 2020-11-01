export const IS_LOCALHOST = true;

// navigatable: 10 < x < 100 || x > 1000 || x in [no child list]
export const PRODUCT_CATEGORIES = [
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
];

