/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.airavata.mft.agent;

import org.apache.airavata.mft.admin.models.TransferState;
import org.apache.airavata.mft.api.service.CallbackEndpoint;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import javax.annotation.PreDestroy;
import java.util.List;
import java.util.concurrent.*;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.PropertySource;

@SpringBootApplication()
@EnableConfigurationProperties
@ConfigurationProperties()
//@PropertySource(value = "classpath:agent-application.properties")
public class MFTAgent implements CommandLineRunner {

    private static final Logger logger = LoggerFactory.getLogger(MFTAgent.class);

    @org.springframework.beans.factory.annotation.Value("${agent.id}")
    private String agentId;

    @Value("${agent.id}")
    private String agentId2;

    @org.springframework.beans.factory.annotation.Value("${agent.host}")
    private String agentHost;

    @org.springframework.beans.factory.annotation.Value("${agent.http.port}")
    private Integer agentHttpPort;

    @org.springframework.beans.factory.annotation.Value("${agent.https.enabled}")
    private boolean agentHttpsEnabled;

    private final Semaphore mainHold = new Semaphore(0);

    public void init() {

    }

    private void handleCallbacks(List<CallbackEndpoint> callbackEndpoints, String transferId, TransferState transferState) {
        if (callbackEndpoints != null && !callbackEndpoints.isEmpty()) {
            for (CallbackEndpoint cbe : callbackEndpoints) {
                switch (cbe.getType()) {
                    case HTTP:
                        break;
                    case KAFKA:
                        break;
                }
            }
        }
    }

    @PreDestroy
    public void stop() {
        logger.info("Stopping Agent " + agentId);
        mainHold.release();
    }

    public void start() throws Exception {
        init();
    }

    @Override
    public void run(String... args) throws Exception {
        logger.info("Starting Agent " + agentId);
        start();
        mainHold.acquire();
        logger.info("Agent exited");
    }

    public static void main(String args[]) throws Exception {
        System.setProperty("spring.config.name", "agent-application");
        SpringApplication.run(MFTAgent.class);
    }
}
