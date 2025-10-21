# 🎨 Современный Казахский Дизайн - Руководство

## Концепция дизайна

Новый дизайн сайта Фонда "Астана" вдохновлен традиционными казахскими мотивами, переосмысленными в современном ключе. Дизайн сочетает:

- **Национальную идентичность** - использование цветов флага Казахстана (голубой и золотой)
- **Современность** - чистые линии, плавные переходы, минимализм
- **Функциональность** - удобная навигация, читаемость, отзывчивость

---

## 🎨 Цветовая палитра

### Основные цвета

```css
--primary-blue: #00A0DC        /* Основной голубой (флаг Казахстана) */
--primary-gold: #D4AF37        /* Золотой (символ богатства культуры) */
--accent-turquoise: #00B8A9    /* Акцентная бирюза */
--accent-terracotta: #E87461   /* Терракотовый акцент */
```

### Нейтральные оттенки

```css
--neutral-cream: #F5F1E8       /* Кремовый фон */
--neutral-sand: #E8DCC4        /* Песочный */
--light-gold: #F4E5C2          /* Светло-золотой */
--white: #FFFFFF               /* Белый */
```

### Текст

```css
--dark-blue: #003B5C           /* Темно-синий для заголовков */
--text-dark: #2C3E50           /* Основной текст */
--text-light: #6B7280          /* Второстепенный текст */
```

---

## ✨ Ключевые дизайн-элементы

### 1. Градиенты

Используются плавные градиенты для создания глубины:

```css
/* Пример: кнопки */
background: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-turquoise) 100%);

/* Пример: заголовки */
background: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-turquoise) 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

### 2. Казахские орнаменты

Тонкие геометрические паттерны используются как фоновые элементы:

```css
background: url("data:image/svg+xml,...");
opacity: 0.5;
```

### 3. Скругленные углы

Современные мягкие формы:

```css
border-radius: 24px;  /* Карточки */
border-radius: 30px;  /* Большие секции */
border-radius: 50px;  /* Кнопки */
```

### 4. Тени и глубина

Многослойные тени для создания объема:

```css
box-shadow: 0 10px 40px rgba(0, 160, 220, 0.1);  /* Спокойная */
box-shadow: 0 20px 60px rgba(0, 160, 220, 0.2);  /* При наведении */
```

---

## 🎯 Типографика

### Шрифты

- **Заголовки**: QazFont (казахский шрифт)
- **Текст**: QazFont, Segoe UI (fallback)

### Размеры

```css
/* Главные заголовки */
font-size: 36px;
font-weight: 800;
letter-spacing: -1px;

/* Подзаголовки */
font-size: 20-24px;
font-weight: 700;

/* Основной текст */
font-size: 16px;
line-height: 1.6-1.9;
```

---

## 🔘 Интерактивные элементы

### Кнопки

**Основная кнопка (Золотая)**
```css
background: linear-gradient(135deg, var(--primary-gold) 0%, var(--accent-terracotta) 100%);
border: 3px solid var(--white);
border-radius: 50px;
transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
```

**Hover эффект**
```css
transform: translateY(-5px) scale(1.05);
box-shadow: 0 12px 35px rgba(212, 175, 55, 0.5);
```

### Карточки

```css
background: linear-gradient(135deg, var(--white) 0%, var(--neutral-cream) 100%);
border-radius: 24px;
transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
```

**Hover анимация**
```css
transform: translateY(-12px) scale(1.02);
```

---

## 📱 Адаптивность

Дизайн полностью адаптивен:

- **Desktop**: > 768px - полная версия
- **Tablet**: 480px - 768px - средние экраны
- **Mobile**: < 480px - компактная версия

---

## 🌟 Специальные секции

### 1. Верхняя полоса
Градиентная полоса в цветах флага:
```css
height: 5px;
background: linear-gradient(90deg, 
    var(--primary-blue) 0%, 
    var(--accent-turquoise) 25%, 
    var(--primary-gold) 50%,
    var(--accent-turquoise) 75%, 
    var(--primary-blue) 100%);
```

### 2. Навигация
Современная навигация с эффектом glassmorphism:
```css
background: linear-gradient(135deg, rgba(245, 241, 232, 0.9) 0%, rgba(255, 255, 255, 0.95) 100%);
backdrop-filter: blur(10px);
border-radius: 50px;
```

### 3. Волонтерская секция
Яркая привлекающая внимание секция с паттерном:
```css
background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-turquoise) 50%,
    var(--primary-blue) 100%);
```

### 4. Футер
Темный градиентный фут с golden акцентами:
```css
background: linear-gradient(135deg, var(--dark-blue) 0%, var(--primary-blue) 100%);
border-top: 5px solid var(--primary-gold);
```

---

## 💫 Анимации

### Плавные переходы
```css
transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
```

### Hover эффекты
- **Карточки**: поднимаются и масштабируются
- **Кнопки**: поднимаются с увеличением тени
- **Изображения**: плавное масштабирование
- **Ссылки**: подчеркивание появляется слева направо

---

## 📋 Рекомендации по использованию

1. **Придерживайтесь цветовой палитры** - используйте CSS переменные
2. **Сохраняйте единообразие** - применяйте одинаковые border-radius и shadows
3. **Используйте плавные анимации** - cubic-bezier для естественности
4. **Добавляйте казахские паттерны** - тонко, как фон
5. **Тестируйте на всех устройствах** - адаптивность критична

---

## 🎨 Примеры использования

### Создание карточки
```css
.my-card {
    background: linear-gradient(135deg, var(--white) 0%, var(--neutral-cream) 100%);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 40px rgba(0, 160, 220, 0.1);
    border: 1px solid rgba(0, 160, 220, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.my-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(0, 160, 220, 0.15);
}
```

### Создание кнопки
```css
.my-button {
    padding: 14px 35px;
    background: linear-gradient(135deg, var(--primary-gold) 0%, var(--accent-terracotta) 100%);
    color: var(--white);
    border: 3px solid var(--white);
    border-radius: 50px;
    font-weight: 700;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4);
}

.my-button:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 12px 35px rgba(212, 175, 55, 0.5);
}
```

---

**Создано:** 2025
**Дизайнер:** AI UI/UX Designer
**Для:** Фонд содействия развитию дружбы народов и национальных культур "АСТАНА"

