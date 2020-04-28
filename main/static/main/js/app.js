document.addEventListener("DOMContentLoaded", function () {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }

  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }

  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function (e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;



      // TODO: get data from inputs and show them in summary
      // Inputs
      const gifts = this.$form.querySelectorAll('input.category:checked');
      const bags = this.$form.querySelector('input#bags');
      const institute = this.$form.querySelector('input#institution:checked');
      const address = this.$form.querySelector('input#address');
      const city = this.$form.querySelector('input#city');
      const postcode = this.$form.querySelector('input#postcode');
      const phone = this.$form.querySelector('input#phone');
      const date = this.$form.querySelector('input#date');
      const time = this.$form.querySelector('input#time');
      const moreInfo = this.$form.querySelector('textarea#more_info');

      // summary fields
      let bagsSummary = this.$form.querySelector('div.summary span#bags');
      let instituteSummary = this.$form.querySelector('div.summary span#institute');
      const addressSummary = this.$form.querySelectorAll('#where > li');
      const dateSummary = this.$form.querySelectorAll('#when > li');
      const giftsArray = (giftsList) => {
        let gifts = '';
        for (let i = 0; i < giftsList.length; i++) {
          if (i !== giftsList.length - 1) {
            gifts += giftsList[i].value + ', ';
          } else {
            gifts += giftsList[i].value;
          }
        }
        return gifts;
      }

      const getDataFromInputs = () => {
        bagsSummary.innerHTML = `${bags.value} worków zawierających: ${giftsArray(gifts)}`;
        instituteSummary.innerHTML = `Dla: ${institute.value}`;
        addressSummary[0].innerHTML = address.value;
        addressSummary[1].innerHTML = city.value;
        addressSummary[2].innerHTML = postcode.value;
        addressSummary[3].innerHTML = phone.value;
        dateSummary[0].innerHTML = date.value;
        dateSummary[1].innerHTML = time.value;
        dateSummary[2].innerHTML = moreInfo.value;
      }

      getDataFromInputs();
      // fill summary fields with values from input elements
      const btnSubmit = $('.submit-form');
      btnSubmit.on('click', function () {
        $.ajax({
          url: 'add_donation/',
          type: 'POST',
          data: {
            'quantity': bags.value,
            'categories': giftsArray(gifts),
            'institution': institute.value,
            'address': address.value,
            'phone': phone.value,
            'city': city.value,
            'zipcode': postcode.value,
            'pick_up_date': date.value,
            'pick_up_time': time.value,
            'pick_up_comment': moreInfo.value,
          },
          success: function () {
            console.log('it works!')
          }
        })
        })
      console.log(btnSubmit);


      // bagsSummary.innerText = this.$form.querySelector('input#bags').value;
      // for (let i = 0; i < gifts.length; i++) {
      //     bagsSummary.innerText += gifts[i].innerText;
      // }
      // instituteSummary.innerText = this.$form.querySelector('div.title').innerText;
    }



    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    // addDonation() {
    //   console.log('it works');
    //   $.ajax({
    //     url: 'add_donation/',
    //     type: 'POST',
    //     data: {
    //       quantity: bags.value,
    //
    //     }
    //   }).done(function (result) {
    //     console.log(result);
    //   })
    // }

    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
      // this.addDonation();
    }
  }

  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});
