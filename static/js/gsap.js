gsap.registerPlugin(ScrollTrigger);

gsap.to(".steps", {duration: 1, scrollTrigger: {
    trigger: ".steps",
    start: "70% bottom",
    markers: false,
}, x: 0, stagger: 0.3});

gsap.to(".req-p", {duration: 1, scrollTrigger: {
    trigger: ".requirements",
    start: "70% bottom",
    markers: false,
}, x: 0, stagger: 0.3});

gsap.to(".ben", {duration: 1, scrollTrigger: {
    trigger: ".benefits",
    start: "50% bottom",
    markers: false,
}, x: 0, stagger: 0.3});

gsap.to(".ex-p", {duration: 1, scrollTrigger: {
    trigger: ".expectations",
    start: "70% bottom",
    markers: false,
}, x: 0, stagger: 0.3});

gsap.to(".bec", {duration: 1, scrollTrigger: {
    trigger: ".bec",
    start: "50% bottom",
    markers: false,
},delay: 1, opacity: 1});

gsap.to(".bec", {duration: 2, scrollTrigger: {
    trigger: ".bec",
    start: "50% bottom",
    markers: false,
}, delay: 1.5, backgroundColor: "rgb(98, 183, 211)", color: "white"});

gsap.to("#form", {duration: 1, scrollTrigger: {
    trigger: ".form",
    start: "50% bottom",
    markers: false,
}, opacity: 1});

gsap.to(".become", {duration: 3, opacity: 1});

gsap.to(".bg", {duration: 1, transform: "translateY(0)", opacity: 1});

gsap.to(".CEO-img", {duration: 1, delay: 1, transform: "translateY(0)", opacity: 1});

gsap.to(".who-we-are", {duration: 1, scrollTrigger: {
    trigger: ".who-we-are",
    start: "50% bottom",
    markers: false,
}, opacity: 1});