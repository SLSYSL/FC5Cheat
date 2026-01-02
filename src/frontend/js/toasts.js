/* JavaScript
Toasts.js
类型: 显示前端 Toasts
*/
class SimpleToast extends HTMLElement {
    constructor() {
        super();

        // 创建 Shadow DOM 实现封装
        this.attachShadow({ mode: 'open' });

        // 定义组件的 HTML 结构
        this.shadowRoot.innerHTML = `
                    <style>
                        :host {
                            display: none;
                            position: fixed;
                            top: 20px;
                            right: 20px;
                            z-index: 1000;
                            box-sizing: border-box;
                        }
                        
                        .toast-container {
                            min-width: 300px;
                            max-width: 400px;
                            padding: 14px 20px;
                            background-color: white;
                            border-radius: 6px;
                            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                            border-left: 4px solid #0078d4; /* 默认蓝色边框 */
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            transform: translateX(100px);
                            opacity: 0;
                            transition: transform 0.3s ease-out, opacity 0.3s ease-out;
                        }
                        
                        .toast-container.show {
                            transform: translateX(0);
                            opacity: 1;
                        }
                        
                        .toast-message {
                            flex-grow: 1;
                            margin: 0;
                            font-size: 14px;
                            color: #323130;
                            line-height: 1.5;
                        }
                        
                        .close-btn {
                            background: none;
                            border: none;
                            color: #605e5c;
                            font-size: 20px;
                            cursor: pointer;
                            padding: 0 0 0 12px;
                            line-height: 1;
                        }
                        
                        .close-btn:hover {
                            color: #323130;
                        }
                        
                        /* 不同类型 Toast 的样式 */
                        .success {
                            border-left-color: #107c10;
                        }
                        
                        .error {
                            border-left-color: #d13438;
                        }
                    </style>
                    
                    <div class="toast-container">
                        <p class="toast-message"></p>
                        <button class="close-btn" aria-label="关闭">&times;</button>
                    </div>
                `;

        // 获取内部元素引用
        this.container = this.shadowRoot.querySelector('.toast-container');
        this.messageEl = this.shadowRoot.querySelector('.toast-message');
        this.closeBtn = this.shadowRoot.querySelector('.close-btn');

        // 绑定关闭按钮事件
        this.closeBtn.addEventListener('click', () => this.hide());
    }

    /**
     * 显示 Toast
     * @param {string} message - 要显示的消息
     * @param {object} options - 配置选项
     * @param {number} options.duration - 显示持续时间（毫秒），默认 3000
     * @param {string} options.type - 类型：'default', 'success', 'error'
     */
    show(message, options = {}) {
        const { duration = 3000, type = 'default' } = options;

        // 设置消息内容
        this.messageEl.textContent = message;

        // 重置并应用类型样式
        this.container.classList.remove('success', 'error');
        if (type !== 'default') {
            this.container.classList.add(type);
        }

        // 显示组件
        this.style.display = 'block';

        // 触发动画（下一帧执行）
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                this.container.classList.add('show');
            });
        });

        // 设置自动关闭
        if (duration > 0) {
            clearTimeout(this._autoHideTimeout);
            this._autoHideTimeout = setTimeout(() => {
                this.hide();
            }, duration);
        }

        return this;
    }

    /**
     * 隐藏 Toast
     */
    hide() {
        this.container.classList.remove('show');

        // 等待动画完成后完全隐藏
        setTimeout(() => {
            this.style.display = 'none';
        }, 300); // 匹配 CSS 过渡时间
    }

    /**
     * 静态方法：快速创建并显示 Toast
     * @param {string} message - 要显示的消息
     * @param {object} options - 配置选项
     * @returns {SimpleToast} Toast 实例
     */
    static makeText(message, options = {}) {
        // 创建 Toast 元素
        const toast = document.createElement('simple-toast');

        // 添加到页面 body
        if (!document.querySelector('simple-toast')) {
            document.body.appendChild(toast);
        } else {
            // 如果已存在 Toast，使用现有的
            const existingToast = document.querySelector('simple-toast');
            existingToast.show(message, options);
            return existingToast;
        }

        // 显示 Toast
        toast.show(message, options);

        return toast;
    }
}

// 注册自定义元素
customElements.define('simple-toast', SimpleToast);