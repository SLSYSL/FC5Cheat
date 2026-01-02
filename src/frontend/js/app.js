/* JavaScript
app.js
类型: 修改器函数转发
*/

document.addEventListener('DOMContentLoaded', function () {
    const lock = document.getElementById("Lock");
    lock.addEventListener("click", async function () {
        await callCheatAPI(true, 'handle_connect_game', true);
    });

    const oxygen = document.getElementById("Oxygen");
    oxygen.addEventListener("change", async function () {
        await callCheatAPI(oxygen, 'handle_oxygen_mode');
    });

    const stamina = document.getElementById("Stamina");
    stamina.addEventListener("change", async function () {
        await callCheatAPI(stamina, 'handle_stamina_mode');
    })

    const noclip = document.getElementById("Noclip");
    noclip.addEventListener("change", async function () {
        await callCheatAPI(noclip, 'handle_noclip_mode');
    })

    const stealth = document.getElementById("Stealth");
    stealth.addEventListener("change", async function () {
        await callCheatAPI(stealth, 'handle_stealth_mode');
    });

    function disableAllSwitches() {
        if (oxygen) oxygen.checked = false;
        if (stamina) stamina.checked = false;
        if (stealth) stealth.checked = false;
        if (noclip) noclip.checked = false;
    }

    const unlock = document.getElementById("Unlock");
    unlock.addEventListener("click", async function () {
        disableAllSwitches();
        await callCheatAPI(false, 'handle_connect_game', true);
    });
});
