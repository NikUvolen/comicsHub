'use strict';

const switch_btns = document.getElementsByClassName('switch_btn');
const register_form = document.getElementById('register-form');
const signin_form = document.getElementById('signin-form');

register_form.style.display = "block";
signin_form.style.display = "none";

for (let i=0; i < switch_btns.length; i++) {
    switch_btns[i].addEventListener('click', (event) => {
        for (let i=0; i < switch_btns.length; i++)
        {
            switch_btns[i].classList.remove('switch_btn-active')
            switch_btns[i].form.style.display = 'none';
        }
        event.target.classList.add('switch_btn-active');
        switch_btns[i].form.style.display = 'block';
    })
}
