document.addEventListener('DOMContentLoaded', () => {

    // --- Элементы DOM ---
    const taskInput = document.getElementById('task-input');
    const addTaskForm = document.getElementById('add-task-form');
    const taskList = document.getElementById('task-list');

    // --- Статичные данные ---
    // Это наш "источник правды". Все изменения в UI будут основаны на этом массиве.
    let tasks = [
        { id: 1, text: 'Купить молоко', completed: true },
        { id: 2, text: 'Позвонить маме', completed: false },
        { id: 3, text: 'Прочитать главу книги по JS', completed: false },
        { id: 4, text: 'Сделать утреннюю зарядку', completed: true },
    ];

    // --- Функция для отрисовки задач ---
    function renderTasks() {
        // Очищаем текущий список
        taskList.innerHTML = '';

        // Если задач нет, показываем сообщение
        if (tasks.length === 0) {
            taskList.innerHTML = '<li class="task-item" style="justify-content: center; color: #888;">Список задач пуст!</li>';
            return;
        }

        // Создаем и добавляем каждый элемент задачи в список
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.className = 'task-item';
            li.dataset.id = task.id; // Используем data-атрибут для связи с данными

            if (task.completed) {
                li.classList.add('completed');
            }

            // Иконки SVG для кнопок
            const editIcon = `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.5L15.232 5.232z"></path></svg>`;
            const deleteIcon = `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>`;

            li.innerHTML = `
                <div class="task-item-content">
                    <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                    <span class="task-text">${task.text}</span>
                </div>
                <div class="task-actions">
                    <button class="action-btn edit-btn">${editIcon}</button>
                    <button class="action-btn delete-btn">${deleteIcon}</button>
                </div>
            `;

            taskList.appendChild(li);
        });
    }

    // --- Обработчики событий ---

    // Добавление новой задачи
    addTaskForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Предотвращаем стандартное поведение формы

        const taskText = taskInput.value.trim();
        if (taskText === '') return; // Не добавляем пустую задачу

        const newTask = {
            id: Date.now(), // Уникальный ID на основе времени
            text: taskText,
            completed: false
        };

        tasks.push(newTask);
        taskInput.value = ''; // Очищаем поле ввода
        renderTasks(); // Перерисовываем список
    });

    // Обработка кликов на списке задач (делегирование событий)
    taskList.addEventListener('click', (e) => {
        const target = e.target;
        const taskItem = target.closest('.task-item'); // Находим родительский элемент задачи

        if (!taskItem) return; // Клик был не по задаче

        const taskId = Number(taskItem.dataset.id);

        // Клик по чекбоксу или тексту (отметить как выполненную)
        if (target.classList.contains('task-checkbox') || target.classList.contains('task-text')) {
            const task = tasks.find(t => t.id === taskId);
            if (task) {
                task.completed = !task.completed;
                renderTasks();
            }
        }

        // Клик по кнопке "Удалить"
        if (target.closest('.delete-btn')) {
            // Фильтруем массив, оставляя все задачи, кроме удаляемой
            tasks = tasks.filter(task => task.id !== taskId);
            renderTasks();
        }

        // Клик по кнопке "Редактировать"
        if (target.closest('.edit-btn')) {
            const task = tasks.find(t => t.id === taskId);
            if (task) {
                const newText = prompt('Редактировать задачу:', task.text);
                if (newText !== null && newText.trim() !== '') {
                    task.text = newText.trim();
                    renderTasks();
                }
            }
        }
    });

    // --- Начальная отрисовка ---
    renderTasks();
});