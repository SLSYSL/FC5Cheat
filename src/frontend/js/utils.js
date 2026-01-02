/* JavaScript
utils.js
类型: 修改器函数调用后端
*/
window.callCheatAPI = async function (id, api, is_read = false) {
    try {
        let isEnabled;
        if (is_read) {
            isEnabled = id;
        } else {
            isEnabled = id.checked;
        }
        const apiMethod = pywebview.api[api];
        let type = 'success';
        if (typeof apiMethod !== 'function') {
            type = 'error';
            throw new Error(`API方法 "${api}" 不存在，请检查方法名是否正确`);
        }
        const response = await apiMethod(isEnabled)
        if (response.code === -1) {
            type = 'error';
        }
        SimpleToast.makeText(response.msg, {
            type: type
        });
    } catch (error) {
        SimpleToast.makeText(error.message, {
            type: 'error'
        });
    }
}