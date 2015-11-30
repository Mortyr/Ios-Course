//
//  ViewController.swift
//  Harjoitus1
//
//  Created by Tonny on 26.11.2015.
//  Copyright © 2015 Tonny. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var RedBg: UIImageView!
    @IBOutlet weak var BlueBG: UIImageView!
    @IBOutlet weak var RedTxt: UIButton!
    @IBOutlet weak var BlueTxt: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func HideBlue(sender: AnyObject) {
        BlueBG.hidden = true
    }

}

