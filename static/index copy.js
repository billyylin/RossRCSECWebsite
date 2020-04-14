// $(function(){
// $("#iteminclude").click(function(){
//   $("#leftItem a").each(function(){
//     var clone = $(this).clone();
//     var mainclick = $(this);
//     clone.children("i").remove();
//     clone.prepend("<i class='material-icons checkedboxicon'>check_box</i>")
//     .append("<span><i class='material-icons deleteicon'>indeterminate_check_box</i></span>")
//     .click(function(){
//       mainclick.show();
//       $(this).remove("a");
//     });
//     $("#rightItem").append(clone);
//     $(this).hide();
//   });
// });
// });

    // $(document).ready(function(){
    //   $("a").click(function(){
    //     $(this).hide();
    // $(function(){
    //   $("#leftItem").children("a").click(function(){
    //     var clone = $(this).clone();
    //     var mainclick = $(this);
    //     // clone.append("<span style='color:red; font-weight:bold; cursor:pointer'>X</span>")
    //     clone.children("i").remove();
    //     clone.prepend("<i class='material-icons checkedboxicon'>check_box</i>")
    //     .append("<span><i class='material-icons deleteicon'>indeterminate_check_box</i></span>")
    //     .click(function(){
    //       mainclick.show();
    //       // var clone2 = $(this).clone();
    //       // clone2.find("a")
    //       // $("#mainItem").append(clone2);
    //       $(this).remove("a");
    //     });
    //     $("#rightItem").append(clone);
    //     $(this).hide();
    //   });
    // });


    // $(function(){
    //   $("#clearallitembtn").click(function(){
    //     $("#rightItem a").each(function(){
    //       $(this).remove();
    //     });
    //     $("#leftItem a").show();
    //   });
    // });







    // variables.push($('#textbox'+counterN).val());

var variable = [];

    $(function(){
      var count = 0;
      console.log(count);
      // var variables = new Dictionary(); //selected variable list to pass info into the conditional statement part
      // var variable = {};
      $("#mainItem").children("a").click(function(){
        count += 1;
        console.log(count);
            if (count > 0){
                  $('#whole-conditional-statements-box').show();
                  $('#conditionalinstruction').hide();
                } else{
                  $('#whole-conditional-statements-box').hide();
                  $('#conditionalinstruction').show();
                };
        var clone = $(this).clone();
        var mainclick = $(this);
        // clone.append("<span style='color:red; font-weight:bold; cursor:pointer'>X</span>")
        clone.children("i").remove();
        var variable_text = clone.text();
        console.log(variable_text);
        // variable[variable_text]="in"; //add a to the varaible list dictionary
        variable.push(variable_text);
        document.getElementById("selected_variable").value= variable;
        console.log(variable);

        $('.conditional_statement_varaible_select').empty();
        $.each(variable, function(i, p) {
            console.log(p);
            // $('#conditional_statement_varaible_select').append($('<a class="dropdown-item"></a>').val(p).html(p));
            // 这里去掉了.val(p)的部分
            $('.conditional_statement_varaible_select').append($('<a class="dropdown-item"></a>').val(p).html(p));
        });

        // make selected item text show up in the top button
        $('.conditional_statement_varaible_select a').click(function(){
          $('#dropdownMenuButton_variable').text($(this).text());
          // ***query reveiw 部分暂时不做
          // var query_line =
          // $('#querypreview').text($(query_line).text());
        });


        clone.prepend("<i class='material-icons checkedboxicon'>check_box</i><a name='selecteditem' value='x'></a>")
        .append("<span><i class='material-icons deleteicon'>indeterminate_check_box</i></span>")
        .click(function(){
          count -= 1;
          console.log(count);
                  if (count > 0){
                        $('#whole-conditional-statements-box').show();
                        $('#conditionalinstruction').hide();
                        // $('#conditional_statement_varaible_select').children("a").remove();
                      } else{
                        $('#whole-conditional-statements-box').hide();
                        $('#conditionalinstruction').show();
                      };
          mainclick.show();

          // var test = mainclick.children("i").remove();
          // var test2 = clone.children("i").remove();
          // console.log(test);
          // console.log(clone);

          // var transfer = clone.children("i").remove()
          // var mainclick_text = transfer.text();
          // console.log(mainclick_text);
          // delete variable[variable_text];  //delete the element from the variable list dictionary
          variable.splice( variable.indexOf(variable_text), 1 );
          document.getElementById("selected_variable").value= variable;
          console.log(variable);
          $(this).remove("a");

          var json_trans = {};
          for (var i = 0 ; i < variable.length; i++) {
              json_trans["position" + (i+1)] = variable[i];
          };
          console.log(json_trans);
          var x = JSON.stringify(json_trans);
          console.log(x);
          // var json_final = JSON.parse(json_trans);

          $('#conditional_statement_varaible_select').empty();
          $.each(variable, function(i, p) {
              console.log(p)
              $('#conditional_statement_varaible_select').append($('<a class="dropdown-item"></a>').val(p).html(p));
          });

        });
        $("#selectedItem").append(clone);
        $(this).hide();

        var json_trans = {};
        for (var i = 0 ; i < variable.length; i++) {
            json_trans["position" + (i+1)] = variable[i];
        };
        console.log(json_trans);
        var x = JSON.stringify(json_trans);
        console.log(x);
        // var json_final = JSON.parse(json_trans);

      });
    });

    // $(function()){
    //   for (var key in variable){
    //     if (variable.hasOwnProperty(key)){
    //       console.log(key);
    //       $('#conditional_statement_varaible_select').append('<a class="dropdown-item" href="#">key</a>');
    //     };
    //   };
    // };

    $(function(){
      $("#selectallbtn").click(function(){
        $('#whole-conditional-statements-box').show();
        $('#conditionalinstruction').hide();
        $("#mainItem a").each(function(){
          var clone = $(this).clone();
          var mainclick = $(this);
          // variables.push($(this).val());
          clone.children("i").remove();
          var variable_text = clone.text();//new
          variable.push(variable_text);//new
          document.getElementById("selected_variable").value= variable;
          console.log(variable)
          clone.prepend("<i class='material-icons checkedboxicon'>check_box</i>")
          .append("<span><i class='material-icons deleteicon'>indeterminate_check_box</i></span>")
          .click(function(){
            mainclick.show();
            $(this).remove("a");
          });
          $("#selectedItem").append(clone);
          $(this).hide();

          $('#conditional_statement_varaible_select').empty();
          $.each(variable, function(i, p) {
              console.log(p)
              $('#conditional_statement_varaible_select').append($('<a class="dropdown-item"></a>').val(p).html(p));
          });

          var json_trans = {};
          for (var i = 0 ; i < variable.length; i++) {
              json_trans["position" + (i+1)] = variable[i];
          };
          console.log(json_trans);
          var x = JSON.stringify(json_trans);
          console.log(x);
          // var json_final = JSON.parse(json_trans);


        });
      });
    });


    $(function(){
      $("#clearallbtn").click(function(){
        $('#whole-conditional-statements-box').hide();
        $('#conditionalinstruction').show();
        $("#selectedItem a").each(function(){
          $(this).remove();
        });
        $("#mainItem a").show();
        variable= [];
        document.getElementById("selected_variable").value= variable;
        console.log(variable);

        $('#conditional_statement_varaible_select').empty();
        $.each(variable, function(i, p) {
            console.log(p)
            $('#conditional_statement_varaible_select').append($('<a class="dropdown-item"></a>').val(p).html(p));
        });

        var json_trans = {};
        for (var i = 0 ; i < variable.length; i++) {
            json_trans["position" + (i+1)] = variable[i];
        };
        console.log(json_trans);
        var x = JSON.stringify(json_trans);
        console.log(x);
        // var json_final = JSON.parse(json_trans);
      });
    });

    // url = 'http://127.0.0.1:5050/output'
    // response = requests.post(url, json=json);

    // const data = {   content : [] }
    // //loop over and push all the data in content data.content.push({ "username" : "harish", "password" : "harish123" });
    // const jsonData = JSON.stringify(data);
    //
    // const fs = require('fs'); fs.writeFile('myjsonfile.json', jsonData, 'utf8', callback);


    $(function(){
      $("#final_submit").click(function(){

      var obj = {'a':'a', 'b':'b'};
      var json_final = JSON.stringify(obj);
      console.log(json_final);
      //
      // var fs = require('fs');
      // fs.writeFile('myjsonfile.json', json_final);
      });
    });



    // var form;
    //
    // form.onsubmit = function (e) {
    //   // stop the regular form submission
    //   e.preventDefault();
    //   var obj = {
    //        table: []
    //     };
    //     obj.table.push({id: 1, square:2});
    //     var json = JSON.stringify(obj);
    //
    //   // collect the form data while iterating over the inputs
    //   // var data = {};
    //   // for (var i = 0, ii = form.length; i < ii; ++i) {
    //   //   var input = form[i];
    //   //   if (input.name) {
    //   //     data[input.name] = input.value;
    //   //   }
    //   // }
    //
    //   // construct an HTTP request
    //   var xhr = new XMLHttpRequest();
    //   xhr.open(form.method, form.action, true);
    //   xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    //
    //   // send the collected data as JSON
    //   xhr.send(JSON.stringify(json));
    //
    //   xhr.onloadend = function () {
    //     // done
    //   };
    // };






      //
      // // var json_str = JSON.stringify(json_trans);
      // var fs = require("fs");
      // var fileContent = "hello";
      // fs.writeFile("./sample.txt", fileContent, (err) => {
      // // fs.writeFile("variableListSample.txt",fileContent, (err) => {
      //     if (err) {
      //         console.error(err);
      //         return;
      //     };
      //     console.log("File has been created");
      // });


    // var json_trans1 = {'a':'a', 'b':'b'}

// $.post("app.py", { json_string:JSON.stringify(json) });

    // function doWork() {
    // 	// ajax the JSON to the server
    // 	$.post("output", variable, function(){
    // 	});
    // 	// stop link reloading the page
    //  event.preventDefault();
    // }



///////////////////////////////////////// 这部分应该没有用 /////////////////////////////////////////
    //dropdown menu text
    // $('#conditional_statement_varaible_select a').click(function(){
    //   $('#dropdownMenuButton_selected').text($(this).text());
    // });



    // $(function(){
    //   $("#conditional_statement_varaible_select a").click(function(){
    //     $("#dropdownMenuButton_selected").text($(this).text());
    //      $("#dropdownMenuButton_selected").val($(this).text());
    //   });
    // });


    // $(".dropdown-menu li a").click(function(){
    //   $(".btn:first-child").html($(this).text()+' <span class="caret"></span>');
    // });

    // $("#conditional_statement_varaible_select >a").on('click',function(){
    //     var val=$(this).html();
    //     $("#test >button").text($(this).text());
    //     $("#test >button").val($(this).text());
    //     // $("#test >button").html(val);
    // })


//////////////////////////////////////////////////////////////////////////////////

$(function(){
  var item = null;

  document.addEventListener('dragstart', function(e)
  {
    item = e.target;

    e.dataTransfer.setData('text', '');

  }, false);

  for(var
    items = document.querySelectorAll('[data-draggable="item"]'),
    len = items.length,
    i = 0; i < len; i ++)
  {
    items[i].setAttribute('draggable', 'true');
    items[i].setAttribute('aria-grabbed', 'false');
    items[i].setAttribute('tabindex', '0');
  }

  for(var
    targets = document.querySelectorAll('[data-draggable="target"]'),
    len = targets.length,
    i = 0; i < len; i ++)
  {
    targets[i].setAttribute('aria-dropeffect', 'none');
  }



  (function()
  {

      //exclude older browsers by the features we need them to support
      //and legacy opera explicitly so we don't waste time on a dead browser
      if
      (
          !document.querySelectorAll
          ||
          !('draggable' in document.createElement('span'))
          ||
          window.opera
      )
      { return; }

      //get the collection of draggable targets and add their draggable attribute
      for(var
          targets = document.querySelectorAll('[data-draggable="target"]'),
          len = targets.length,
          i = 0; i < len; i ++)
      {
          targets[i].setAttribute('aria-dropeffect', 'none');
      }

      //get the collection of draggable items and add their draggable attributes
      for(var
          items = document.querySelectorAll('[data-draggable="item"]'),
          len = items.length,
          i = 0; i < len; i ++)
      {
          items[i].setAttribute('draggable', 'true');
          items[i].setAttribute('aria-grabbed', 'false');
          items[i].setAttribute('tabindex', '0');
      }



      //dictionary for storing the selections data
      //comprising an array of the currently selected items
      //a reference to the selected items' owning container
      //and a refernce to the current drop target container
      var selections =
      {
          items      : [],
          owner      : null,
          droptarget : null
      };

      //function for selecting an item
      function addSelection(item)
      {
          //if the owner reference is still null, set it to this item's parent
          //so that further selection is only allowed within the same container
          if(!selections.owner)
          {
              selections.owner = item.parentNode;
          }

          //or if that's already happened then compare it with this item's parent
          //and if they're not the same container, return to prevent selection
          else if(selections.owner != item.parentNode)
          {
              return;
          }

          //set this item's grabbed state
          item.setAttribute('aria-grabbed', 'true');

          //add it to the items array
          selections.items.push(item);
      }

      //function for unselecting an item
      function removeSelection(item)
      {
          //reset this item's grabbed state
          item.setAttribute('aria-grabbed', 'false');

          //then find and remove this item from the existing items array
          for(var len = selections.items.length, i = 0; i < len; i ++)
          {
              if(selections.items[i] == item)
              {
                  selections.items.splice(i, 1);
                  break;
              }
          }
      }

      //function for resetting all selections
      function clearSelections()
      {
          //if we have any selected items
          if(selections.items.length)
          {
              //reset the owner reference
              selections.owner = null;

              //reset the grabbed state on every selected item
              for(var len = selections.items.length, i = 0; i < len; i ++)
              {
                  selections.items[i].setAttribute('aria-grabbed', 'false');
              }

              //then reset the items array
              selections.items = [];
          }
      }

      //shorctut function for testing whether a selection modifier is pressed
      function hasModifier(e)
      {
          return (e.ctrlKey || e.metaKey || e.shiftKey);
      }


      //function for applying dropeffect to the target containers
      function addDropeffects()
      {
          //apply aria-dropeffect and tabindex to all targets apart from the owner
          for(var len = targets.length, i = 0; i < len; i ++)
          {
              if
              (
                  targets[i] != selections.owner
                  &&
                  targets[i].getAttribute('aria-dropeffect') == 'none'
              )
              {
                  targets[i].setAttribute('aria-dropeffect', 'move');
                  targets[i].setAttribute('tabindex', '0');
              }
          }

          //remove aria-grabbed and tabindex from all items inside those containers
          for(var len = items.length, i = 0; i < len; i ++)
          {
              if
              (
                  items[i].parentNode != selections.owner
                  &&
                  items[i].getAttribute('aria-grabbed')
              )
              {
                  items[i].removeAttribute('aria-grabbed');
                  items[i].removeAttribute('tabindex');
              }
          }
      }

      //function for removing dropeffect from the target containers
      function clearDropeffects()
      {
          //if we have any selected items
          if(selections.items.length)
          {
              //reset aria-dropeffect and remove tabindex from all targets
              for(var len = targets.length, i = 0; i < len; i ++)
              {
                  if(targets[i].getAttribute('aria-dropeffect') != 'none')
                  {
                      targets[i].setAttribute('aria-dropeffect', 'none');
                      targets[i].removeAttribute('tabindex');
                  }
              }

              //restore aria-grabbed and tabindex to all selectable items
              //without changing the grabbed value of any existing selected items
              for(var len = items.length, i = 0; i < len; i ++)
              {
                  if(!items[i].getAttribute('aria-grabbed'))
                  {
                      items[i].setAttribute('aria-grabbed', 'false');
                      items[i].setAttribute('tabindex', '0');
                  }
                  else if(items[i].getAttribute('aria-grabbed') == 'true')
                  {
                      items[i].setAttribute('tabindex', '0');
                  }
              }
          }
      }

      //shortcut function for identifying an event element's target container
      function getContainer(element)
      {
          do
          {
              if(element.nodeType == 1 && element.getAttribute('aria-dropeffect'))
              {
                  return element;
              }
          }
          while(element = element.parentNode);

          return null;
      }



      //mousedown event to implement single selection
      document.addEventListener('mousedown', function(e)
      {
          //if the element is a draggable item
          if(e.target.getAttribute('draggable'))
          {
              //clear dropeffect from the target containers
              clearDropeffects();

              //if the multiple selection modifier is not pressed
              //and the item's grabbed state is currently false
              if
              (
                  !hasModifier(e)
                  &&
                  e.target.getAttribute('aria-grabbed') == 'false'
              )
              {
                  //clear all existing selections
                  clearSelections();

                  //then add this new selection
                  addSelection(e.target);
              }
          }

          //else [if the element is anything else]
          //and the selection modifier is not pressed
          else if(!hasModifier(e))
          {
              //clear dropeffect from the target containers
              clearDropeffects();

              //clear all existing selections
              clearSelections();
          }

          //else [if the element is anything else and the modifier is pressed]
          else
          {
              //clear dropeffect from the target containers
              clearDropeffects();
          }

      }, false);

      //mouseup event to implement multiple selection
      document.addEventListener('mouseup', function(e)
      {
          //if the element is a draggable item
          //and the multipler selection modifier is pressed
          if(e.target.getAttribute('draggable') && hasModifier(e))
          {
              //if the item's grabbed state is currently true
              if(e.target.getAttribute('aria-grabbed') == 'true')
              {
                  //unselect this item
                  removeSelection(e.target);

                  //if that was the only selected item
                  //then reset the owner container reference
                  if(!selections.items.length)
                  {
                      selections.owner = null;
                  }
              }

              //else [if the item's grabbed state is false]
              else
              {
                  //add this additional selection
                  addSelection(e.target);
              }
          }

      }, false);

      //dragstart event to initiate mouse dragging
      document.addEventListener('dragstart', function(e)
      {
          //if the element's parent is not the owner, then block this event
          if(selections.owner != e.target.parentNode)
          {
              e.preventDefault();
              return;
          }

          //[else] if the multiple selection modifier is pressed
          //and the item's grabbed state is currently false
          if
          (
              hasModifier(e)
              &&
              e.target.getAttribute('aria-grabbed') == 'false'
          )
          {
              //add this additional selection
              addSelection(e.target);
          }

          //we don't need the transfer data, but we have to define something
          //otherwise the drop action won't work at all in firefox
          //most browsers support the proper mime-type syntax, eg. "text/plain"
          //but we have to use this incorrect syntax for the benefit of IE10+
          e.dataTransfer.setData('text', '');

          //apply dropeffect to the target containers
          addDropeffects();

      }, false);



      //keydown event to implement selection and abort
      document.addEventListener('keydown', function(e)
      {
          //if the element is a grabbable item
          if(e.target.getAttribute('aria-grabbed'))
          {
              //Space is the selection or unselection keystroke
              if(e.keyCode == 32)
              {
                  //if the multiple selection modifier is pressed
                  if(hasModifier(e))
                  {
                      //if the item's grabbed state is currently true
                      if(e.target.getAttribute('aria-grabbed') == 'true')
                      {
                          //if this is the only selected item, clear dropeffect
                          //from the target containers, which we must do first
                          //in case subsequent unselection sets owner to null
                          if(selections.items.length == 1)
                          {
                              clearDropeffects();
                          }

                          //unselect this item
                          removeSelection(e.target);

                          //if we have any selections
                          //apply dropeffect to the target containers,
                          //in case earlier selections were made by mouse
                          if(selections.items.length)
                          {
                              addDropeffects();
                          }

                          //if that was the only selected item
                          //then reset the owner container reference
                          if(!selections.items.length)
                          {
                              selections.owner = null;
                          }
                      }

                      //else [if its grabbed state is currently false]
                      else
                      {
                          //add this additional selection
                          addSelection(e.target);

                          //apply dropeffect to the target containers
                          addDropeffects();
                      }
                  }

                  //else [if the multiple selection modifier is not pressed]
                  //and the item's grabbed state is currently false
                  else if(e.target.getAttribute('aria-grabbed') == 'false')
                  {
                      //clear dropeffect from the target containers
                      clearDropeffects();

                      //clear all existing selections
                      clearSelections();

                      //add this new selection
                      addSelection(e.target);

                      //apply dropeffect to the target containers
                      addDropeffects();
                  }

                  //else [if modifier is not pressed and grabbed is already true]
                  else
                  {
                      //apply dropeffect to the target containers
                      addDropeffects();
                  }

                  //then prevent default to avoid any conflict with native actions
                  e.preventDefault();
              }

              //Modifier + M is the end-of-selection keystroke
              if(e.keyCode == 77 && hasModifier(e))
              {
                  //if we have any selected items
                  if(selections.items.length)
                  {
                      //apply dropeffect to the target containers
                      //in case earlier selections were made by mouse
                      addDropeffects();

                      //if the owner container is the last one, focus the first one
                      if(selections.owner == targets[targets.length - 1])
                      {
                          targets[0].focus();
                      }

                      //else [if it's not the last one], find and focus the next one
                      else
                      {
                          for(var len = targets.length, i = 0; i < len; i ++)
                          {
                              if(selections.owner == targets[i])
                              {
                                  targets[i + 1].focus();
                                  break;
                              }
                          }
                      }
                  }

                  //then prevent default to avoid any conflict with native actions
                  e.preventDefault();
              }
          }

          //Escape is the abort keystroke (for any target element)
          if(e.keyCode == 27)
          {
              //if we have any selected items
              if(selections.items.length)
              {
                  //clear dropeffect from the target containers
                  clearDropeffects();

                  //then set focus back on the last item that was selected, which is
                  //necessary because we've removed tabindex from the current focus
                  selections.items[selections.items.length - 1].focus();

                  //clear all existing selections
                  clearSelections();

                  //but don't prevent default so that native actions can still occur
              }
          }

      }, false);



      //related variable is needed to maintain a reference to the
      //dragleave's relatedTarget, since it doesn't have e.relatedTarget
      var related = null;

      //dragenter event to set that variable
      document.addEventListener('dragenter', function(e)
      {
          related = e.target;

      }, false);

      //dragleave event to maintain target highlighting using that variable
      document.addEventListener('dragleave', function(e)
      {
          //get a drop target reference from the relatedTarget
          var droptarget = getContainer(related);

          //if the target is the owner then it's not a valid drop target
          if(droptarget == selections.owner)
          {
              droptarget = null;
          }

          //if the drop target is different from the last stored reference
          //(or we have one of those references but not the other one)
          if(droptarget != selections.droptarget)
          {
              //if we have a saved reference, clear its existing dragover class
              if(selections.droptarget)
              {
                  selections.droptarget.className =
                      selections.droptarget.className.replace(/ dragover/g, '');
              }

              //apply the dragover class to the new drop target reference
              if(droptarget)
              {
                  droptarget.className += ' dragover';
              }

              //then save that reference for next time
              selections.droptarget = droptarget;
          }

      }, false);

      //dragover event to allow the drag by preventing its default
      document.addEventListener('dragover', function(e)
      {
          //if we have any selected items, allow them to be dragged
          if(selections.items.length)
          {
              e.preventDefault();
          }

      }, false);



      //dragend event to implement items being validly dropped into targets,
      //or invalidly dropped elsewhere, and to clean-up the interface either way
      document.addEventListener('dragend', function(e)
      {
          //if we have a valid drop target reference
          //(which implies that we have some selected items)
          if(selections.droptarget)
          {
              //append the selected items to the end of the target container
              for(var len = selections.items.length, i = 0; i < len; i ++)
              {
                  selections.droptarget.appendChild(selections.items[i]);
              }

              //prevent default to allow the action
              e.preventDefault();
          }

          //if we have any selected items
          if(selections.items.length)
          {
              //clear dropeffect from the target containers
              clearDropeffects();

              //if we have a valid drop target reference
              if(selections.droptarget)
              {
                  //reset the selections array
                  clearSelections();

                  //reset the target's dragover class
                  selections.droptarget.className =
                    selections.droptarget.className.replace(/ dragover/g, '');

                  //reset the target reference
                  selections.droptarget = null;
              }
          }

      }, false);

  })();








  // function handleDragStart(e) {
  //   this.style.opacity = '0.4';  // this / e.target is the source node.
  // }
  // var cols = document.querySelectorAll('.draggablebox');
  // [].forEach.call(cols, function(col) {
  //   col.addEventListener('dragstart', handleDragStart, false);
  // });
  //
  // function handleDragOver(e) {
  //   if (e.preventDefault) {
  //     e.preventDefault(); // Necessary. Allows us to drop.
  //   }
  //
  //   e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.
  //
  //   return false;
  // }
  //
  // function handleDragEnter(e) {
  //   // this / e.target is the current hover target.
  //   this.classList.add('over');
  // }
  //
  // function handleDragLeave(e) {
  //   this.classList.remove('over');  // this / e.target is previous target element.
  // }
  //
  // function handleDrop(e) {
  //   // this / e.target is current target element.
  //
  //   if (e.stopPropagation) {
  //     e.stopPropagation(); // stops the browser from redirecting.
  //   }
  //
  //   // See the section on the DataTransfer object.
  //
  //   return false;
  // }
  //
  // function handleDragEnd(e) {
  //   // this/e.target is the source node.
  //
  //   [].forEach.call(cols, function (col) {
  //     col.classList.remove('over');
  //   });
  // }
  //
  // var cols = document.querySelectorAll('.draggablebox');
  // [].forEach.call(cols, function(col) {
  //   col.addEventListener('dragstart', handleDragStart, false);
  //   col.addEventListener('dragenter', handleDragEnter, false);
  //   col.addEventListener('dragover', handleDragOver, false);
  //   col.addEventListener('dragleave', handleDragLeave, false);
  //   col.addEventListener('drop', handleDrop, false);
  //   col.addEventListener('dragend', handleDragEnd, false);
  // });



})



///////////////////////////////////////////////////////////////////////////////////


$(function(){
  $(".statementdeletebtn").click(function(){
    $(this).parent().parent().remove();
  });
});

$(function(){
  $("#removegroup").click(function(){
    $(this).parent().parent().parent().remove();
  });
});



$(function(){
  $(".add-one-rule-btn").click(function(){
    $(this).parent().parent().siblings(".statement-part")
    .append('<div class="oneconditionalstatement col-md-12 draggablebox" draggable="true" data-draggable = "item">\
    <!-- dropdown menu begin -->\
    <div class="form-inline justify-content-between">\
    <div class="dropdown col-md-3">\
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
        Select the Variable\
      </button>\
      <div class="dropdown-menu dropdown_in_conditional_state" aria-labelledby="dropdownMenuButton" id="conditional_statement_varaible_select">\
        <a class="dropdown-item" href="#">Action</a>\
        <a class="dropdown-item" href="#">Another action</a>\
        <a class="dropdown-item" href="#">Something else here</a>\
      </div>\
    </div>\
    <!-- dropdown menu end -->\
    <!-- dropdown menu begin -->\
    <div class="dropdown col-md-3">\
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton_logic" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
        Select the Logic\
      </button>\
      <div class="dropdown-menu dropdown_in_conditional_state" aria-labelledby="dropdownMenuButton_logic">\
        <a class="dropdown-item">equal</a>\
        <a class="dropdown-item">not equal</a>\
        <a class="dropdown-item">begins with</a>\
        <a class="dropdown-item">doesn\'t begins with</a>\
        <a class="dropdown-item">contains</a>\
        <a class="dropdown-item">doesn\'t contains</a>\
        <a class="dropdown-item">ends with</a>\
        <a class="dropdown-item">doesn\'t ends with</a>\
        <a class="dropdown-item">is empty</a>\
        <a class="dropdown-item">is not empty</a>\
        <a class="dropdown-item">is null</a>\
        <a class="dropdown-item">is not null</a>\
      </div>\
    </div>\
    <!-- dropdown menu end -->\
    <input type="text" class="form-control col-md-4">\
    <button type="button" class="btn btn-danger btn-sm col-md-1 statementdeletebtn">Delete</button>\
  </div>\
</div>\
<script>\
$(function(){\
  $(".statementdeletebtn").click(function(){\
    $(this).parent().parent().remove();\
  });\
});\
$(function(){\
$(".dropdown_in_conditional_state a").click(function(){\
  $(this).parent().siblings().text($(this).text());\
});\
});\
</script>\
')
});
});



// $(function(){
//   $(".add-one-group-btn").click(function(){
//     $(this).parent().parent().siblings(".statement-part")
//     .append('<div class="conditionalstatements container" id="whole-conditional-statements-box">\
//       <div class="row justify-content-between" id="conditional-statement-header">\
//         <div class="btn-group btn-group-toggle col-md-5" data-toggle="buttons" id="logic-condition">\
//           <label class="btn btn-sm btn-outline-primary active">\
//             <input type="radio" name="andorlogic" id="andbtn" autocomplete="off" checked> AND\
//           </label>\
//           <label class="btn btn-sm btn-outline-primary">\
//             <input type="radio" name="andorlogic" id="orbtn" autocomplete="off"> OR\
//           </label>\
//         </div>\
//         <div class="col-md-7" id="remove-add-btns">\
//           <button type="button" class="btn btn-danger btn-sm" id="removeconditionalbtn">Remove the group</button>\
//           <button type="button" class="btn btn-success btn-sm add-one-rule-btn">Add Rule</button>\
//           <button type="button" class="btn btn-success btn-sm add-one-group-btn">Add Group</button>\
//         </div>\
//       </div>\
//     <div class="container justify-content-end statement-part" data-draggable = "target">\
//         ::before\
//         <div class="oneconditionalstatement col-md-12 draggablebox" draggable="true" data-draggable = "item">\
//             <!-- dropdown menu begin -->\
//             <div class="form-inline justify-content-between">\
//             <div class="dropdown col-md-3">\
//               <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
//                 Select the Variable\
//               </button>\
//               <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\
//                 <a class="dropdown-item" href="#">Action</a>\
//                 <a class="dropdown-item" href="#">Another action</a>\
//                 <a class="dropdown-item" href="#">Something else here</a>\
//               </div>\
//             </div>\
//             <!-- dropdown menu end -->\
//             <!-- dropdown menu begin -->\
//             <div class="dropdown col-md-3">\
//               <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
//                 Select the Logic\
//               </button>\
//               <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\
//                 <a class="dropdown-item" href="#">equal</a>\
//                 <a class="dropdown-item" href="#">not equal</a>\
//                 <a class="dropdown-item" href="#">begins with</a>\
//                 <a class="dropdown-item" href="#">doesn\'t begins with</a>\
//                 <a class="dropdown-item" href="#">contains</a>\
//                 <a class="dropdown-item" href="#">doesn\'t contains</a>\
//                 <a class="dropdown-item" href="#">ends with</a>\
//                 <a class="dropdown-item" href="#">doesn\'t ends with</a>\
//                 <a class="dropdown-item" href="#">is empty</a>\
//                 <a class="dropdown-item" href="#">is not empty</a>\
//                 <a class="dropdown-item" href="#">is null</a>\
//                 <a class="dropdown-item" href="#">is not null</a>\
//               </div>\
//             </div>\
//             <!-- dropdown menu end -->\
//             <input type="text" class="form-control col-md-4">\
//             <button type="button" class="btn btn-danger btn-sm col-md-1" id="deletestatementbtn">Delete</button>\
//           </div>\
//         </div>\
//     </div>\
//     </div>');
//   });
// });

$(function(){
  $(".add-one-group-btn").click(function(){
    $(this).parent().parent().siblings(".statement-part")
    .append('<div class="conditionalstatements container col-md-12" id="conditionalstatements">\
        <div class="row justify-content-between conditional-statement-header">\
          <div class="btn-group btn-group-toggle col-md-5" data-toggle="buttons">\
            <label class="btn btn-sm btn-outline-primary active">\
              <input type="radio" name="andorlogic" id="andbtn" autocomplete="off" checked> AND\
            </label>\
            <label class="btn btn-sm btn-outline-primary">\
              <input type="radio" name="andorlogic" id="orbtn" autocomplete="off"> OR\
            </label>\
          </div>\
          <div class="col-md-auto justify-content-end">\
            <button type="button" class="btn btn-danger btn-sm" id="removegroup">Remove the Group</button>\
            <button type="button" class="btn btn-success btn-sm add-one-rule-btn">Add Rule</button>\
            <button type="button" class="btn btn-success btn-sm add-one-group-btn">Add Group</button>\
          </div>\
        </div>\
      <div class="container justify-content-end statement-part" data-draggable = "target">\
      <!-- <div class="row justify-content-end col-md-11"> -->\
      <!-- <div class="col-md-1 conditionalline">\
      </div> -->\
      <div class="oneconditionalstatement row col-md-12 draggablebox" draggable="true" data-draggable = "item">\
          <!-- dropdown menu begin -->\
          <div class="form-inline justify-content-between">\
          <div class="dropdown col-md-3">\
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
              Select the Variable\
            </button>\
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\
              <a class="dropdown-item" href="#">Action</a>\
              <a class="dropdown-item" href="#">Another action</a>\
              <a class="dropdown-item" href="#">Something else here</a>\
            </div>\
          </div>\
          <!-- dropdown menu end -->\
          <!-- dropdown menu begin -->\
          <div class="dropdown col-md-3">\
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\
              Select the Logic\
            </button>\
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\
              <a class="dropdown-item" href="#">equal</a>\
              <a class="dropdown-item" href="#">not equal</a>\
              <a class="dropdown-item" href="#">begins with</a>\
              <a class="dropdown-item" href="#">doesn\'t begins with</a>\
              <a class="dropdown-item" href="#">contains</a>\
              <a class="dropdown-item" href="#">doesn\'t contains</a>\
              <a class="dropdown-item" href="#">ends with</a>\
              <a class="dropdown-item" href="#">doesn\'t ends with</a>\
              <a class="dropdown-item" href="#">is empty</a>\
              <a class="dropdown-item" href="#">is not empty</a>\
              <a class="dropdown-item" href="#">is null</a>\
              <a class="dropdown-item" href="#">is not null</a>\
            </div>\
          </div>\
          <!-- dropdown menu end -->\
          <input type="text" class="form-control col-md-4" id="conditiontext">\
          <button type="button" class="btn btn-danger btn-sm col-md-1 statementdeletebtn">Delete</button>\
        </div>\
      </div>\
    </div>');
  });
});
